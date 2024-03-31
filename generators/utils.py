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
