"""
Module to store already generated outputs and generate a Graph object.
This generator is used to generate a graph from a file avoiding to generate the 
random graph again, and enables to validate if the graph/tree is correct.
"""
import pickle
from models.graph import Graph, Node
from generators import utils


def generate_graph_from_one_random_file() -> Graph:
    # List all .dot files in outputs folder

    list_of_files = utils.get_files_in_folder('outputs')
    random_file = list_of_files[0]
    # Read the first file
    graph = utils.read_graph_from_file(f"outputs/{random_file}")
    pass

def generate_graph_for_all_files_in_folder(dump: bool = False) -> list:
    list_of_files = utils.get_files_in_folder('outputs')
    list_of_graphs = list()
    for file in list_of_files:
        graph = utils.read_graph_from_file(f"outputs/{file}")
        print(f"Graph: {graph.name}")
        list_of_graphs.append(graph)
    
    if dump:
        pickle.dump(list_of_graphs, open("outputs/graphs.pkl", "wb"))
    return list_of_graphs

def generate_graph_for_all_files_and_add_weight() -> list:
    list_of_files = utils.get_files_in_folder('outputs')
    list_of_graphs = list()
    for file in list_of_files:
        graph = utils.read_graph_from_file(f"outputs/{file}", add_random_weigth=True)
        print(f"Graph: {graph.name}")
        list_of_graphs.append(graph)
    return list_of_graphs

def load_graphs_from_file() -> list:
    return pickle.load(open("outputs/graphs.pkl", "rb"))

if __name__ == "__main__":
    # graphs = generate_graph_for_all_files_and_add_weight()
    graphs = generate_graph_for_all_files_in_folder()
    # Sort by graph.name
    graphs.sort(key=lambda x: x.name)
    names = [graph.name for graph in graphs]
    for graph in graphs:
        # print(f"Graph: {graph.name}")
        print(f"Calculating MST Directed for {graph.name}")
        kruskal_mst=graph.get_MST_by_kruskal_direct()
        # kruskal_mst.save_graphviz_with_weigth(is_dijkstra=True)
    breakpoint()
    