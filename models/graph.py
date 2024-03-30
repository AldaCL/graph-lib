"""
Node class for graph
"""
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Node:
    """
    Node class to represent a node in a graph
    :param value: value to identify of the node   
    """
    def __init__(self, name: str):        
        self.name = f'N_{name}'
        self.edges = list()

    def add_edge(self, edge) -> None:
        """append the edge to the list of edges of the node
        so we can know the edges that are connected to the node"""
        self.edges.append(edge)

    def get_degree(self) -> int:
        """ 
        return the degree of the node, which is 
        the number of edges connected to the node
        """
        return len(self.edges)

    def __repr__(self) -> str:
        return f"{self.name}"
    
    def __eq__(self, other) -> bool:
        return self.name == other.name
    
@dataclass
class Edge:
    """
    Edge class to represent an edge in a graph
    :param weigth: weigth of the edge
    :param node_from: starting node of the edge
    :param node_to: ending node of the edge
    """
    def __init__(self, node_from: Node, node_to: Node, weigth: int=1):
        self.weigth = weigth
        self.node_from = node_from
        self.node_to = node_to
        self.add_to_nodes()

    def add_to_nodes(self):
        """
        call the add_edge method of the node_from and node_to
        to add the edge to the list of edges of the nodes
        """
        self.node_from.add_edge(self)
        self.node_to.add_edge(self)

    def get_nodes(self):
        """
        return the tuple of nodes connected by the edge
        (node_from, node_to)
        """
        return (self.node_from, self.node_to)

    def __repr__(self):
        return f"{self.node_from.name} -> {self.node_to.name}; \n"

    def __cmp__(self, other):
        return (self.node_from.name == other.node_from.name and self.node_to.name == other.node_to.name) or (self.node_from.name == other.node_to.name and self.node_to.name == other.node_from.name)
    
    def __eq__(self, other) -> bool:
        return (self.node_from.name == other.node_from.name and self.node_to.name == other.node_to.name) or (self.node_from.name == other.node_to.name and self.node_to.name == other.node_from.name)
    
@dataclass
class DirectedEdge:
    """
    Edge class to represent an edge in a graph
    :param weigth: weigth of the edge
    :param node_from: starting node of the edge
    :param node_to: ending node of the edge
    """
    def __init__(self, node_from: Node, node_to: Node, weigth: int=1):
        self.weigth = weigth
        self.node_from = node_from
        self.node_to = node_to
        self.add_to_nodes()

    def add_to_nodes(self):
        """
        call the add_edge method of the node_from and node_to
        to add the edge to the list of edges of the nodes
        """
        self.node_from.add_edge(self)
        self.node_to.add_edge(self)

    def get_nodes(self):
        """
        return the tuple of nodes connected by the edge
        (node_from, node_to)
        """
        return (self.node_from, self.node_to)

    def __repr__(self):
        return f"{self.node_from.name} -> {self.node_to.name}; \n"

    def __cmp__(self, other):
        return self.node_from.name == other.node_from.name and self.node_to.name == other.node_to.name
    
    def __eq__(self, other) -> bool:
        return self.node_from.name == other.node_from.name and self.node_to.name == other.node_to.name
    
    

class Graph:
    """
    Graph class to represent a graph with a 
    list of nodes and edges
    :param nodes: list of nodes in the graph
    :param edges: list of edges in the graph
    """
    def __init__(self,
                 nodes: list=None,
                 edges: list=None,
                 is_directed: bool= False,
                 name: str="GenericGraph"):
        self.name = name
        self.is_directed = is_directed
        if nodes is None:
            nodes = []
        if edges is None:
            edges = []
        self.nodes = nodes
        self.edges = edges
    
    def add_node(self, node: Node) -> None:
        """
        Insert a node to the list of nodes in the graph
        :param node: node to be inserted
        """
        self.nodes.append(node)
        
    def save_graphviz(self, filename:str = "") -> str:
        """
        Save the graph to a txt file in graphViz format
        """
        current_datetime_code = datetime.now().strftime("%Y%m%d%H%M")
        if filename == "":
            filename = f"graph_{self.name}_{current_datetime_code}.dot"
        else: 
            filename = f"{filename}_{current_datetime_code}.dot"

        fileroute = f"outputs/{filename}"
        
        with open(fileroute, "w", encoding="UTF") as file:
            file.write(f"graph {self.name}" + "{\n")
            for edge in self.edges:
                file.write(edge.__repr__())
            file.write("}")

        print(f"Graph saved to {fileroute} ")
    
    def save_graphviz_by_node(self, filename:str = "") -> str:
        """
        Save the graph to a txt file in graphViz format
        """
        current_datetime_code = datetime.now().strftime("%Y%m%d%H%M")
        if filename == "":
            filename = f"graph_{self.name}_{current_datetime_code}.dot"
        else: 
            filename = f"{filename}_{current_datetime_code}.dot"
            
        fileroute = f"outputs/{filename}"
        
        printed_edges = list()
        with open(fileroute, "w", encoding="UTF") as file:
            file.write(f"graph {self.name}" + "{\n")
            for node in self.nodes:
                if node.get_degree() > 0:
                    for edge in node.edges:
                        if edge not in printed_edges:
                            printed_edges.append(edge)
                            file.write(edge.__repr__())
                else:
                    file.write(f"{node.name}; \n")
            file.write("}")

        print(f"Graph saved to {fileroute} ")
    
    def __str__(self):
        for edge in self.edges:
            return edge.__repr__()
        
        
class DirectedGraph:
    """
    Graph class to represent a graph with a 
    list of nodes and edges
    :param nodes: list of nodes in the graph
    :param edges: list of edges in the graph
    """
    def __init__(self,
                 nodes: list=None,
                 edges: list=None,
                 is_directed: bool= False,
                 name: str="GenericGraph"):
        self.name = name
        self.is_directed = is_directed
        if nodes is None:
            nodes = []
        if edges is None:
            edges = []
        self.nodes = nodes
        self.edges = edges
    
    def add_node(self, node: Node) -> None:
        """
        Insert a node to the list of nodes in the graph
        :param node: node to be inserted
        """
        self.nodes.append(node)
        
    def save_graphviz(self, filename:str = "") -> str:
        """
        Save the graph to a txt file in graphViz format
        """
        current_datetime_code = datetime.now().strftime("%Y%m%d%H%M")
        if filename == "":
            filename = f"graph_{self.name}_{current_datetime_code}.dot"
        else: 
            filename = f"{filename}_{current_datetime_code}.dot"

        fileroute = f"outputs/{filename}"

        with open(fileroute, "w", encoding="UTF") as file:
            file.write(f"digraph {self.name}" + "{\n")
            for edge in self.edges:
                file.write(edge.__repr__())
            file.write("}")

        print(f"Graph saved to {fileroute} ")
    
    def save_graphviz_by_node(self, filename:str = "") -> str:
        """
        Save the graph to a txt file in graphViz format
        """
        current_datetime_code = datetime.now().strftime("%Y%m%d%H%M")
        if filename == "":
            filename = f"graph_{self.name}_{current_datetime_code}.dot"
        else: 
            filename = f"{filename}_{current_datetime_code}.dot"

        fileroute = f"outputs/{filename}"

        with open(fileroute, "w", encoding="UTF") as file:
            file.write(f"digraph {self.name}" + "{\n")
            for node in self.nodes:
                if node.get_degree() > 0:
                    for edge in node.edges:
                        file.write(edge.__repr__())
                else:
                    file.write(f"{node.name}; \n")
            file.write("}")

        print(f"Graph saved to {fileroute} ")
       
    
    def __str__(self):
        for edge in self.edges:
            return edge.__repr__()