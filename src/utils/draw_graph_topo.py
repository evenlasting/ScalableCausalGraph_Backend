import matplotlib.pyplot as plt
import networkx as nx

def draw_dag(G):
    # 检查图是否是有向无环图
    if not nx.is_directed_acyclic_graph(G):
        raise ValueError("图必须是有向无环图")

    # 拓扑排序
    topo_sort = list(nx.topological_sort(G))
    layers = {}
    for node in topo_sort:
        # 对于每个节点，找到其所有前驱节点的最大层数，然后将其放入下一层
        max_layer = -1
        for pred in G.predecessors(node):
            max_layer = max(max_layer, layers[pred])
        layers[node] = max_layer + 1

    # 确定每层的节点数，以便可以居中对齐
    layer_counts = {}
    for node, layer in layers.items():
        layer_counts[layer] = layer_counts.get(layer, 0) + 1

    # 确定节点位置
    pos = {}
    layer_offsets = {layer: -count / 2 for layer, count in layer_counts.items()}
    for node, layer in layers.items():
        pos[node] = (layer_offsets[layer], -layer)
        layer_offsets[layer] += 1

    nx.draw(G, pos, with_labels=True, node_color='lightblue', arrowstyle='->', arrowsize=10)
    plt.savefig('causal_graph.png')