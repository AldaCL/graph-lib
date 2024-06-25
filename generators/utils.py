""""
utility functions to avoid large class methods
"""
import os

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
    graph = Graph(name = file_path.split("/")[-1].split(".")[0])
    print(f"Reading graph from file: {file_path}")
    with open(file_path, 'r') as f:
        for line in f:
            if line.startswith(('graph', '{', '}')):
                continue
            line = line.strip(' \n').strip(';')
            line = line.replace('->', '').replace("N_","").split()
            if len(line) == 1:
                # Only one node in the line
                # node1 = Node(line[0])
                # node2 = None
                # weight = 1
                continue
            elif len(line) == 2:
                # Two nodes in the line without weight
                node1, node2 = Node(line[0]), Node(line[1])
                weight = 1
            elif len(line) == 3:
                # Two nodes in the line with weight
                node1, node2, weight = Node(line[0]), Node(line[1]), int(line[2])
            graph.add_validated_edge(node1, node2, weight)
    if graph.get_nodes() == []:
        print("Graph is empty")
    return graph


def get_files_in_folder(folder: str = "outputs") -> list:
    """
    Get all files .dot in a folder
    Args:
        folder: folder to search, default to 'outputs'
    Returns:
        list of files in the folder
    """

    list_of_files = list()
    for file in os.listdir(folder):
        if file.endswith(".dot"):
            list_of_files.append(file)
    return list_of_files
