# 使用说明

用途：防止分子 AI 的表示或干预破坏化学、几何、物理、对称性或分子身份语义。

场景：分子生成、扩散、3D conformer、complex、reaction、坐标扰动、decoder、causal probe。

触发：AI 状态或操作直接作用于分子、分子图、3D 坐标、复合物或反应。

最小使用：state semantics -> required molecular constraints -> AI operation -> predicted failure -> cheapest discriminator -> continue/revise/kill。
