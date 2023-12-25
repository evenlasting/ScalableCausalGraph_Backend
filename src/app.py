from fastapi import FastAPI, File, UploadFile
from api.schemas.causal_graph import CausalGraphInput, CausalGraphOutput
from src.services.causal_graph_generator import CausalGraphGenerator
# from src.services.causal_graph_optimizer import CausalGraphOptimizer

app = FastAPI()

@app.post("/generate-causal-graph/", response_model=CausalGraphOutput)
async def generate_causal_graph(file: UploadFile = File(...)):
    # 保存文件并获取文件路径
    file_path = "path/to/saved/file.csv"  # 保存文件的逻辑
    # 生成因果图
    generator = CausalGraphGenerator(file_path)
    causal_graph = generator.generate_causal_graph()
    # 返回响应
    return causal_graph

@app.post("/optimize-causal-graph/", response_model=CausalGraphOutput)
async def optimize_causal_graph(input: CausalGraphInput):
    # 这里假设 CausalGraphInput 包含了原始图及约束条件
    optimizer = CausalGraphOptimizer(input.causal_graph)
    optimizer.apply_constraints(input.constraints)
    optimizer.summarize_graph()
    # 返回优化后的图
    return optimizer.causal_graph
