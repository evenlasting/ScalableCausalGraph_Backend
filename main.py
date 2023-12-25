from src.services.causal_graph_generator import CausalGraphGenerator
import matplotlib.pyplot as plt
import networkx as nx

from src.utils.draw_graph_topo import draw_dag

dag = CausalGraphGenerator("work").generate_causal_graph()
draw_dag(dag)

