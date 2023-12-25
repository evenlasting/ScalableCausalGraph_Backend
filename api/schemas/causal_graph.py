from pydantic import BaseModel
from typing import List

# 示例：表示CSV文件上传的模型
class CausalGraphInput(BaseModel):
    file_path: str  # 文件在服务器上的路径或临时位置

# 定义一个超级节点及其包含的节点
class SuperNode(BaseModel):
    id: int  # 超级节点的唯一标识符
    contains: List[int]  # 包含的原始节点ID列表

# 定义超级节点之间的边
class SuperEdge(BaseModel):
    source: int  # 源超级节点ID
    target: int  # 目标超级节点ID
    weight: float  # 边的权重或强度

# 最终的输出模型
class CausalGraphOutput(BaseModel):
    super_nodes: List[SuperNode]
    super_edges: List[SuperEdge]
