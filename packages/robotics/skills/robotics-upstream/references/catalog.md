# Robotics Upstream Catalog

Use this catalog only after `robotics-upstream` has been activated. Prefer a verified local clone over a remote source because local source is faster to inspect and can be pinned to an exact commit.

## Unitree

| Scope | Canonical upstream | Typical use |
|---|---|---|
| SDK / DDS / low-level interfaces | `https://github.com/unitreerobotics/unitree_sdk2.git` | channel APIs, messages, robot services, low-level command/state contracts |
| MuJoCo | `https://github.com/unitreerobotics/unitree_mujoco.git` | official simulation integration and robot models |
| RL baseline | `https://github.com/unitreerobotics/unitree_rl_gym.git` | policy training/deployment conventions |
| MuJoCo/MJLab RL | `https://github.com/unitreerobotics/unitree_rl_mjlab.git` | current Unitree MJLab reinforcement-learning workflow |
| ROS2 integration | `https://github.com/unitreerobotics/unitree_ros2.git` | ROS2/DDS integration, examples, topics and environment setup |

Known verified local clones on this host at skill creation time:

- `/home/ad/unitree_sdk2`
- `/home/ad/unitree_mujoco`
- `/home/ad/unitree_rl_gym`
- `/home/ad/robot/unitree_rl_mjlab`

Do not assume these paths still exist or are current. Run `scripts/discover.py` for every task that needs an upstream reference.

## NVIDIA robotics

| Scope | Canonical upstream | Typical use |
|---|---|---|
| Isaac ROS | `https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_common.git` and repositories under the `NVIDIA-ISAAC-ROS` organization | accelerated ROS2 graph, NITROS, launch/deployment patterns |
| Isaac Lab | `https://github.com/isaac-sim/IsaacLab.git` | robot learning, RL, imitation learning, environment/task structure |
| Isaac Sim | `https://github.com/isaac-sim/IsaacSim.git` | simulation application, ROS2 bridge and simulator behavior |
| GR00T | `https://github.com/NVIDIA/Isaac-GR00T.git` | humanoid/generalist policy training, inference and deployment |

## Selection rule

Choose the narrowest upstream that owns the questioned behavior:

- Unitree device/API/message/mode behavior -> Unitree first.
- Isaac-specific simulation/training/deployment behavior -> NVIDIA first.
- Project wrapper behavior -> current project first, then follow its dependency to the owning upstream.
- A local clone with a non-official origin is not authoritative merely because its directory name matches.

When a local clone exists, record its `HEAD` and `origin` before using it as evidence. If the task depends on latest upstream behavior, explicitly fetch or compare against the remote before treating the local clone as current.