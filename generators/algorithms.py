"""
This python module contains all the core-logic to generate
graphs by different algorithms. The algorithms are implemented
in the form of functions and each function takes a graph object
as an argument and returns a new graph object generated by the
algorithm. The algorithms implemented in this module are:
- Mesh randomd graph 
- Erdos-Renyi random graph
- Gilbert random graph
- Geographical random graph
- Barabasi-Albert varian graph
- Dorogovtsev-Mendes graph
"""
from models.graph import Graph, Node, Edge


def mesh_random_graph(m:int, n:int, is_directed: bool=False, graph_name: str="") -> Graph:
    """
    Generate a graph with ,m*n nodes
    """
    if m < 1 or n < 1:
        print("m and n must be bigger than 1")
        raise ValueError()
    list_of_nodes = list()
    # Create list of nodes
    for column in range(m):
        row_nodes = list()
        for row in range(n):
            node_name = f"{column + 1}{row + 1}"
            node = Node(name=node_name)
            row_nodes.append(node)
        list_of_nodes.append(row_nodes)
    # print("List of nodes: ", list_of_nodes)
    # Flatten list of nodes
    list_of_edges = list()
    for col in range(m):
        for ix in range(n):
            if ix + 1 < n:
                list_of_edges.append(Edge(list_of_nodes[col][ix],list_of_nodes[col][ix+1]))
            if col + 1 < m:
                list_of_edges.append(Edge(list_of_nodes[col][ix],list_of_nodes[col + 1][ix]))
                
    # print("List of edges: ", list_of_edges)
    list_of_nodes = [node for row in list_of_nodes for node in row]
    
    if graph_name == "":
        graph_name = f"Mesh_{m}x{n}"
    graph = Graph(nodes=list_of_nodes,
                  edges=list_of_edges,
                  is_directed=is_directed,
                  name=graph_name)

    graph.save_graphviz(filename=graph_name)
    return graph