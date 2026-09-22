#!/usr/bin/env python3
"""Discover the closest robotics upstream references without mutating repos."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
from pathlib import Path
from typing import Iterable

OFFICIAL_REMOTES = {
    "unitree_sdk2": "https://github.com/unitreerobotics/unitree_sdk2.git",
    "unitree_ros2": "https://github.com/unitreerobotics/unitree_ros2.git",
    "unitree_mujoco": "https://github.com/unitreerobotics/unitree_mujoco.git",
    "unitree_rl_gym": "https://github.com/unitreerobotics/unitree_rl_gym.git",
    "unitree_rl_mjlab": "https://github.com/unitreerobotics/unitree_rl_mjlab.git",
    "isaac_ros_common": "https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_common.git",
    "IsaacLab": "https://github.com/isaac-sim/IsaacLab.git",
    "IsaacSim": "https://github.com/isaac-sim/IsaacSim.git",
    "Isaac-GR00T": "https://github.com/NVIDIA/Isaac-GR00T.git",
}

SEARCH_ROOTS = (
    "~",
    "~/robot",
    "~/src",
    "~/repos",
    "~/projects",
)


def run(*args: str, cwd: Path | None = None) -> str:
    try:
        proc = subprocess.run(
            args,
            cwd=cwd,
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True,
            timeout=5,
        )
    except (OSError, subprocess.TimeoutExpired):
        return ""
    return proc.stdout.strip() if proc.returncode == 0 else ""


def git_root(path: Path) -> Path | None:
    out = run("git", "rev-parse", "--show-toplevel", cwd=path)
    return Path(out).resolve() if out else None


def git_origin(path: Path) -> str:
    return run("git", "remote", "get-url", "origin", cwd=path)


def git_head(path: Path) -> str:
    return run("git", "rev-parse", "HEAD", cwd=path)


def project_links(root: Path) -> list[dict[str, str]]:
    links: list[dict[str, str]] = []
    origin = git_origin(root)
    if origin:
        links.append({"kind": "project_remote", "path": str(root), "origin": origin})

    modules = run("git", "config", "-f", ".gitmodules", "--get-regexp", r"^submodule\..*\.path$", cwd=root)
    if not modules:
        return links

    for line in modules.splitlines():
        try:
            key, relative = line.split(None, 1)
        except ValueError:
            continue
        name = key.removeprefix("submodule.").removesuffix(".path")
        url = run("git", "config", "-f", ".gitmodules", "--get", f"submodule.{name}.url", cwd=root)
        links.append(
            {
                "kind": "project_submodule",
                "name": name,
                "path": str((root / relative).resolve()),
                "origin": url,
            }
        )
    return links


def candidate_dirs() -> Iterable[Path]:
    names = set(OFFICIAL_REMOTES)
    patterns = ("unitree*", "*isaac*", "*Isaac*", "*groot*", "*GR00T*")
    seen: set[Path] = set()
    for raw_root in SEARCH_ROOTS:
        root = Path(os.path.expanduser(raw_root))
        if not root.is_dir():
            continue
        for pattern in patterns:
            for path in root.glob(pattern):
                resolved = path.resolve()
                if resolved in seen or not resolved.is_dir():
                    continue
                if resolved.name in names or any(token in resolved.name.lower() for token in ("unitree", "isaac", "groot")):
                    seen.add(resolved)
                    yield resolved


def normalize_remote(url: str) -> str:
    normalized = url.strip().lower().removesuffix(".git")
    if normalized.startswith("git@github.com:"):
        normalized = "https://github.com/" + normalized.removeprefix("git@github.com:")
    return normalized


def official_name_for_origin(origin: str) -> str | None:
    norm = normalize_remote(origin)
    for name, canonical in OFFICIAL_REMOTES.items():
        if norm == normalize_remote(canonical):
            return name
    return None


def score(query: str, item: dict[str, str]) -> int:
    q = query.lower().replace("_", "-")
    text = " ".join(item.values()).lower().replace("_", "-")
    name = item.get("name", "").lower().replace("_", "-")

    ownership_terms = {
        "unitree-sdk2": ("dds", "sdk", "low-level", "lowlevel", "motor", "joint", "channel", "message", "service"),
        "unitree-ros2": ("ros2", "topic", "rclcpp", "launch", "cyclonedds", "ros graph"),
        "unitree-mujoco": ("mujoco", "simulation", "simulator", "mjcf"),
        "unitree-rl-gym": ("rl", "reinforcement", "policy", "training", "legged gym"),
        "unitree-rl-mjlab": ("mjlab", "mujoco rl", "reinforcement", "policy", "training"),
        "isaac-ros-common": ("isaac ros", "nitros", "ros2", "nvidia ros", "graph"),
        "isaaclab": ("isaac lab", "reinforcement", "imitation", "training", "environment", "task"),
        "isaacsim": ("isaac sim", "simulation", "simulator", "physx", "omniverse"),
        "isaac-gr00t": ("groot", "gr00t", "vla", "foundation model", "humanoid policy"),
    }

    value = 0
    if "unitree" in q or "g1" in q:
        if "unitree" in text:
            value += 12
    if "isaac" in q or "nvidia" in q or "groot" in q or "gr00t" in q:
        if any(token in text for token in ("isaac", "nvidia", "groot", "gr00t")):
            value += 12

    for repo, terms in ownership_terms.items():
        if repo == name and any(term in q for term in terms):
            value += 25

    for word in (w for w in q.replace("/", " ").replace("-", " ").split() if len(w) > 2):
        if word in text:
            value += 2
    if item.get("official") == "true":
        value += 3
    if item.get("kind") == "project_submodule":
        value += 4
    return value


def main() -> int:
    parser = argparse.ArgumentParser(description="Discover project-linked and official robotics upstream references.")
    parser.add_argument("query", nargs="*", help="robotics task terms used only for ranking")
    parser.add_argument("--workspace", default=os.getcwd(), help="current project/workspace path")
    parser.add_argument("-n", "--limit", type=int, default=8, help="maximum references to print")
    args = parser.parse_args()

    query = " ".join(args.query)
    workspace = Path(args.workspace).expanduser().resolve()
    root = git_root(workspace) or workspace

    items = project_links(root) if root.exists() else []

    for path in candidate_dirs():
        origin = git_origin(path)
        if not origin:
            continue
        official_name = official_name_for_origin(origin)
        items.append(
            {
                "kind": "local_upstream",
                "name": official_name or path.name,
                "path": str(path),
                "origin": origin,
                "head": git_head(path),
                "official": "true" if official_name else "false",
            }
        )

    discovered_officials = {
        item.get("name")
        for item in items
        if item.get("kind") == "local_upstream" and item.get("official") == "true"
    }
    for name, origin in OFFICIAL_REMOTES.items():
        if name not in discovered_officials:
            items.append({"kind": "canonical_remote", "name": name, "origin": origin, "official": "true"})

    ranked = sorted(items, key=lambda item: (-score(query, item), item.get("kind", ""), item.get("name", item.get("path", ""))))
    limit = max(1, args.limit)
    print(json.dumps({"workspace": str(root), "query": query, "references": ranked[:limit]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
