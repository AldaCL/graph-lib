""""
utility functions to avoid large class methods
"""
from models.graph import Graph, Node
from datetime import datetime

def get_distance(node1: Node, node2: Node) -> float:
    """
    Calculate the distance between two nodes
    :param node1: first node
    :param node2: second node
    :return: distance between the nodes
    """
    return ((node1.x_coord - node2.x_coord) ** 2 + (node1.y_coord - node2.y_coord) ** 2) ** 0.5



def read_graph_from_file(file_path: str) -> Graph:
    """
    Read a graph from a file
    :param file_path: path to the file
    :return: graph object
    """
    graph = Graph()
    with open(file_path, 'r') as f:
        for line in f:
            if line.startswith('graph'):
                continue
            node1, node2, weight = line.strip('-> ').split()
            node1 = Node(node1)
            node2 = Node(node2)
            graph.add_edge(node1, node2, float(weight))
    return graph