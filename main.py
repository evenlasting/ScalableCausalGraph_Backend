from src.services.causal_graph_generator import CausalGraphGenerator
import matplotlib.pyplot as plt
import networkx as nx

from src.utils.draw_graph_topo import draw_dag

# dag = CausalGraphGenerator("work").generate_causal_graph()

import pickle

# with open('dag_file.pkl', 'wb') as f:
#     pickle.dump(dag, f)

with open('dag_file.pkl','rb') as f:
    load_dag = pickle.load(f)

nx_graph = load_dag.to_networkx()
# draw_dag(dag)

