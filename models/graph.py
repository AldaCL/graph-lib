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
        self.in_edges = list()
        self.out_edges = list()

    def add_in_edge(self, edge) -> None:
        """append the edge to the list of edges of the node
        so we can know the edges that are connected to the node
        This list will alos be used to non directed graphs to add 
        non directed edges
        """
        self.in_edges.append(edge)

    def add_out_edge(self, edge) -> None:
        """append the edge to the list of edges of the node
        so we can know the edges that are connected to the node"""
        self.out_edges.append(edge)

    def get_degree(self) -> int:
        """ 
        return the degree of the node, which is 
        the number of edges connected to the node
        """
        return len(self.in_edges) + len(self.out_edges)

    def get_indegree(self) -> int:
        """ 
        return the degree of the node, which is 
        the number of edges connected to the node
        """
        return len(self.in_edges)

    def get_outdegree(self) -> int:
        """ 
        return the outdegree of the node, which is 
        the number of edges connected to the node
        """
        return len(self.out_edges)
    
    def __repr__(self) -> str:
        return f"{self.name}"

    def __eq__(self, other) -> bool:
        return self.name == other.name

class GeoNode(Node):
    """
    Node class to represent a node in a graph
    :param value: value to identify of the node   
    """
    def __init__(self, name: str, x_coord: float=0, y_coord: float=0):        
        super().__init__(name)
        self.x_coord = x_coord
        self.y_coord = y_coord

    def calculate_distance(self, other) -> float:
        """"
        Calculate the distance between two nodes
        """
        return ((self.x_coord - other.x_coord) ** 2 + (self.y_coord - other.y_coord) ** 2) ** 0.5
    
    def __repr__(self) -> str:
        return f"{self.name} ({self.x_coord}, {self.y_coord})"

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
        # self.add_to_nodes()

    def add_to_nodes(self):
        """
        call the add_edge method of the node_from and node_to
        to add the edge to the list of edges of the nodes
        """
        self.node_from.add_out_edge(self)
        self.node_to.add_in_edge(self)

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
class DirectedEdge(Edge):
    """
    Edge class to represent an edge in a graph
    :param weigth: weigth of the edge
    :param node_from: starting node of the edge
    :param node_to: ending node of the edge
    """
    def __init__(self, node_from: Node, node_to: Node, weigth: int=1):
        super().__init__(node_from, node_to, weigth)

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
        
    def get_nodes(self) -> list:
        """
        Return the list of nodes in the graph
        """
        return self.nodes
    
    def add_edge(self, from_node: Node, to_node: Node, weight: str="") -> None:
        """
        Insert an edge to the list of edges in the graph
        :param from_node: starting node of the edge
        :param to_node: ending node of the edge
        """
        if self.is_directed:
            edge = DirectedEdge(from_node, to_node, weight)
        else:
            edge = Edge(from_node, to_node, weight)
        if edge not in self.edges:
            edge.add_to_nodes()
            self.edges.append(edge)
    
    def save_graphviz_by_node(self) -> str:
        """
        Save the graph to a txt file in graphViz format
        """
        current_datetime_code = datetime.now().strftime("%Y%m%d%H%M")
        filename = f"graph_{self.name}_{current_datetime_code}.dot"    
        fileroute = f"outputs/{filename}"
        graph_type = "digraph" if self.is_directed else "graph"
        with open(fileroute, "w", encoding="UTF") as file:
            file.write(f"{graph_type} {self.name}" + "{\n")
            for node in self.nodes:
                if node.get_outdegree() > 0:
                    for edge in node.out_edges:    
                        file.write(edge.__repr__())
                else:
                    file.write(f"{node.name}; \n")
            file.write("}")

        print(f"Graph saved to {fileroute} ")
    
    
    def __str__(self):
        for edge in self.edges:
            return edge.__repr__()


    # def save_graphviz(self, filename:str = "") -> str:
    #     """
    #     Save the graph to a txt file in graphViz format
    #     """
    #     current_datetime_code = datetime.now().strftime("%Y%m%d%H%M")
    #     if filename == "":
    #         filename = f"graph_{self.name}_{current_datetime_code}.dot"
    #     else: 
    #         filename = f"{filename}_{current_datetime_code}.dot"

    #     fileroute = f"outputs/{filename}"
        
    #     with open(fileroute, "w", encoding="UTF") as file:
    #         file.write(f"graph {self.name}" + "{\n")
    #         for edge in self.edges:
    #             file.write(edge.__repr__())
    #         file.write("}")

    #     print(f"Graph saved to {fileroute} ")
# class DirectedGraph(Graph):
#     """
#     Graph class to represent a graph with a 
#     list of nodes and edges
#     :param nodes: list of nodes in the graph
#     :param edges: list of edges in the graph
#     """
#     def __init__(self,
#                  nodes: list=None,
#                  edges: list=None,
#                  is_directed: bool= True,
#                  name: str="GenericGraph"):
#         super().__init__(nodes, edges, is_directed, name)
        
#     def save_graphviz(self, filename:str = "") -> str:
#         """
#         Save the graph to a txt file in graphViz format
#         """
#         current_datetime_code = datetime.now().strftime("%Y%m%d%H%M")
#         if filename == "":
#             filename = f"graph_{self.name}_{current_datetime_code}.dot"
#         else: 
#             filename = f"{filename}_{current_datetime_code}.dot"

#         fileroute = f"outputs/{filename}"

#         with open(fileroute, "w", encoding="UTF") as file:
#             file.write(f"digraph {self.name}" + "{\n")
#             for edge in self.edges:
#                 file.write(edge.__repr__())
#             file.write("}")

#         print(f"Graph saved to {fileroute} ")
    
#     def save_graphviz_by_node(self, filename:str = "") -> str:
#         """
#         Save the graph to a txt file in graphViz format
#         """
#         current_datetime_code = datetime.now().strftime("%Y%m%d%H%M")
#         if filename == "":
#             filename = f"graph_{self.name}_{current_datetime_code}.dot"
#         else: 
#             filename = f"{filename}_{current_datetime_code}.dot"

#         fileroute = f"outputs/{filename}"

#         with open(fileroute, "w", encoding="UTF") as file:
#             file.write(f"digraph {self.name}" + "{\n")
#             for node in self.nodes:
#                 if node.get_degree() > 0:
#                     for edge in node.edges:
#                         file.write(edge.__repr__())
#                 else:
#                     file.write(f"{node.name}; \n")
#             file.write("}")

#         print(f"Graph saved to {fileroute} ")
       
