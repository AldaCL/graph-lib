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
        
        Args: 
            edge (Edge): edge to be added to the node
        Examples:
            >>> node = Node('A')
            >>> edge = Edge(Node('A'), Node('B'))
            >>> node.add_in_edge(edge)
        Returns:
            None
        """
        # As long as the edge can be None due to disconnected nodes, is needed to validate if 
        # incomming edge is not none
        if edge:
            self.in_edges.append(edge)

    def add_out_edge(self, edge) -> None:
        """
        append the edge to the list of edges of the node
        so we can know the edges that are connected to the node
        
        Args:
            edge (Edge): edge to be added to the node
        Examples:
            >>> node = Node('A')
            >>> edge = Edge(Node('A'), Node('B'))
            >>> node.add_out_edge(edge)
        Returns:
            None
        """
        if edge:
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
    
    def get_edges(self) -> list:
        """
        return the list of edges connected to the node
        """
        set_of_edges =  list()
        for edge in self.in_edges:
            set_of_edges.append(edge)
                
        for edge in self.out_edges:
            if edge not in set_of_edges:
                set_of_edges.append(edge)
                
        return set_of_edges
    def __repr__(self) -> str:
        return f"{self.name}"

    def __eq__(self, other) -> bool:
        return self.name == other.name
    
    def __hash__(self) -> str:
        return hash(self.name)

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
    
    Attributes:
        node_from (Node): starting node of the edge
        node_to (Node): ending node of the edge
        weigth (int): weigth of the edge
    
    Examples:
        >>> node1 = Node('A')
        >>> node2 = Node('B')
        >>> edge = Edge(node1, node2, 10) # Weigth of 10
        >>> edge_without_weigth = Edge(node1, node2) # Weigth of 1 as default
    """
    def __init__(self, node_from: Node, node_to: Node, weigth: int=1):
        self.weigth = weigth
        self.node_from = node_from
        self.node_to = node_to
        self.alter_color = False
        # self.add_to_nodes()

    def add_to_nodes(self):
        """
        call the add_edge method of the node_from and node_to
        to add the edge to the list of edges of the nodes.
        
        """
        self.node_from.add_out_edge(self)
        self.node_to.add_in_edge(self)

    def get_nodes(self):
        """
        return the tuple of nodes connected by the edge
        (node_from, node_to)
        Args:
            None
        Returns:
            tuple: tuple of nodes connected by the edge
        """
        return (self.node_from, self.node_to)

    def get_connected_node(self, node: Node) -> Node:
        """
        return the node connected to the given node
        Args:
            node (Node): node to compare with the edge nodes
        Returns:
            Node: node connected to the given node
        """
        if self.node_from == node:
            return self.node_to
        elif self.node_to == node:
            return self.node_from
        else:
            return None
    
    def print_with_weight(self)->str:
        """
        return the string representation of the edge with its weight
        Args:
            None
        Returns:
            str: string representation of the edge with its weight
        """
        if self.alter_color:
            return f"{self.node_from.name} -> {self.node_to.name} [label={self.weigth}, color=red]; \n"
        else:
            return f"{self.node_from.name} -> {self.node_to.name} [label={self.weigth}]; \n"
    
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
    Attributes:
        node_from (Node): starting node of the edge
        node_to (Node): ending node of the edge
        weigth (int): weigth of the edge
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
    - Attributes:
        - nodes (list): list of nodes in the graph
        - edges (list): list of edges in the graph
        - is_directed (bool): flag to indicate if the graph is directed
        - name (str): name of the graph
        
    - Examples:
    
        >>> graph = Graph()
        >>> node1 = Node('A')
        >>> node2 = Node('B')
        >>> graph.add_node(node1)
        >>> graph.add_node(node2)
        >>> graph.add_edge(node1, node2)
    """
    def __init__(self,
                 nodes: set=None,
                 edges: list=None,
                 is_directed: bool= False,
                 name: str="GenericGraph"):
        self.name = name
        self.is_directed = is_directed
        if nodes is None:
            nodes = set()
        if edges is None:
            edges = []
        self.nodes = nodes
        self.edges = edges
    
    def add_node(self, node: Node) -> None:
        """
        Insert a node to the list of nodes in the graph.
        Warning: of deprecation Use this methods carefully as it does not check if the node is already in the graph
        Neither connects the node to the graph by adding the edges to the node
        Args:
            node (Node): node to be added to the graph
        Returns:
            None
        Examples:
            >>> graph = Graph()
            >>> node1 = Node('A')
            >>> graph.add_node(node1)
        """
        self.nodes.add(node)
        
    def get_nodes(self) -> list:
        """
        Return the list of nodes in the graph
        """
        return self.nodes
    
    def add_edge(self, from_node: Node, to_node: Node, weight: int= 1) -> None:
        """
        Insert an edge to the list of edges in the graph
        Args:
            from_node (Node): starting node of the edge
            to_node (Node): ending node of the edge
            weight (str): weight of the edge
        Returns:
            None
        Examples:
            >>> graph = Graph()
            >>> node1 = Node('A')
            >>> node2 = Node('B')
            >>> graph.add_edge(node1, node2)
        """
        # Need to validate if the edge is valid. Not valid cases are when from_node and to_node are the same
        # or when any of the nodes are None
        if from_node is None and to_node is None:
            return
        if from_node is None:
            self.add_node(to_node)
            return
        if to_node is None:
            self.add_node(from_node)
            return
        if from_node == to_node:
            # self.add_node(from_node)
            return

        edge_class = DirectedEdge if self.is_directed else Edge
        edge = edge_class(from_node, to_node, int(weight))

        # Check if the edge is already in the list of edges
        # We override the __eq__ method in the Edge class to compare the nodes of the edge
        if edge not in self.edges:
            self.add_node(from_node)
            self.add_node(to_node)
            edge.add_to_nodes()
            self.edges.append(edge)
        
    def add_validated_edge(self, from_node: Node, to_node: Node, weight: int= 1) -> None:
        """
        Insert an edge to the list of edges in the graph. avoid validation of the nodes
        to make the code more efficient
        Args:
            from_node (Node): starting node of the edge
            to_node (Node): ending node of the edge
            weight (str): weight of the edge
        Returns:
            None
        Examples:
            >>> graph = Graph()
            >>> node1 = Node('A')
            >>> node2 = Node('B')
            >>> graph.add_edge(node1, node2)
        """
        # Need to validate if the edge is valid. Not valid cases are when from_node and to_node are the same
        # or when any of the nodes are None
        if from_node is None and to_node is None:
            return
        if from_node is None:
            return
        if to_node is None:
            return
        if from_node == to_node:
            # self.add_node(from_node)
            return

        if from_node in self.nodes:
            from_node = [node for node in self.nodes if node.name == from_node.name][0]
        else:
            self.add_node(from_node)
        if to_node in self.nodes:
            to_node = [node for node in self.nodes if node.name == to_node.name][0]
        else:
            self.add_node(to_node)

        edge_class = DirectedEdge if self.is_directed else Edge
        edge = edge_class(from_node, to_node, int(weight))

        # Check if the edge is already in the list of edges
        # We override the __eq__ method in the Edge class to compare the nodes of the edge
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
        visited_edges = list()
        with open(fileroute, "w", encoding="UTF") as file:
            file.write(f"{graph_type} {self.name}" + "{\n")
            for node in self.nodes:
                if node.get_outdegree() > 0:
                    for edge in node.get_edges():
                        if edge not in visited_edges:
                            file.write(edge.__repr__())
                            visited_edges.append(edge)
                else:
                    # file.write(f"{node.name}; \n")
                    continue
            file.write("}")

        print(f"Graph saved to {fileroute} ")
    
    def save_graphviz_by_edges(self) -> str:
        current_datetime_code = datetime.now().strftime("%Y%m%d%H%M")
        filename = f"graph_{self.name}_{current_datetime_code}.dot"   
        fileroute = f"outputs/{filename}"
        graph_type = "digraph" if self.is_directed else "graph"
        with open(fileroute, "w", encoding="UTF") as file:
            file.write(f"{graph_type} {self.name}" + "{\n")
            for edge in self.edges:
                file.write(edge.__repr__())
            file.write("}")

        print(f"Graph saved to {fileroute} ")


    def save_graphviz_with_weigth(self, is_dijkstra: bool = False) -> str:
        current_datetime_code = datetime.now().strftime("%Y%m%d%H%M")
        if is_dijkstra:
            filename = f"graph_{self.name}_{current_datetime_code}_dijkstra.dot"
        else:
            filename = f"graph_{self.name}_{current_datetime_code}.dot"
        fileroute = f"outputs/{filename}"
        graph_type = "digraph" if self.is_directed else "graph"
        with open(fileroute, "w", encoding="UTF") as file:
            file.write(f"{graph_type} {self.name}" + "{\n")
            for edge in self.edges:
                file.write(edge.print_with_weight())
            file.write("}")

        print(f"Graph saved to {fileroute} ")

    
    
    def __str__(self):
        for edge in self.edges:
            return edge.__repr__()


    def get_bfs_tree(self) -> 'Graph':
        """
        Calculate the breadth first search tree of the graph given an starting node
        Identified by name, to ease the use of the function
 
        - Args:
            - self.nodes: set of nodes in the graph
            
        - Returns:
            - Graph: graph with the BFS tree
        """
        # Get the first node of the graph
        starting_node = [node for node in list(self.nodes) if node.name == 'N_0']
        if not starting_node:
            starting_node = list(self.nodes)[0]
        else:
            starting_node = starting_node[0]
            
        bfs_tree = Graph(name=f"BFS_{self.name}")
        visited = set()
        queue = list()
        queue.append(starting_node)
        
        while queue:
            current_node = queue.pop(0)
            visited.add(current_node)
            for edge in current_node.get_edges():
                connected_node = edge.get_connected_node(current_node)
                if connected_node not in visited:
                    queue.append(connected_node)
                    bfs_tree.add_edge(current_node, connected_node)
                    visited.add(connected_node)
        return bfs_tree
    
    def get_dfs_recursive(self, starting_node_index: int = 0) -> 'Graph':
        """
        Calculate the depth first search tree of the graph given an starting node
        Identified by name, to ease the use of the function
        If not starting_node_name is given, then starting node will be the first element of the list of nodes.
        Also can be given the index of the starting node in the list of nodes and that 
        will be the starting node.
        Args:
            starting_node_name (str): name of the starting node
            starting_node_index (int): index of the starting node
        Returns:
            Graph: graph with the DFS tree
        """
        starting_node = list(self.nodes)[starting_node_index]
        dfs_tree = Graph(name=f"DFS_R_{self.name}")
        visited = set()
        def dfs_recursive(node):
            visited.add(node)
            dfs_tree.add_node(node)
            for edge in node.get_edges():
                connected_node = edge.get_connected_node(node)
                if connected_node not in visited:
                    dfs_tree.add_edge(node, connected_node)
                    dfs_recursive(connected_node)
        dfs_recursive(starting_node)
        return dfs_tree
    
    def get_dfs_iterative(self, starting_node_index: int = 0) -> 'Graph':
        """
        Calculate the depth first search tree of the graph given an starting node
        Identified by name, to ease the use of the function
        If not starting_node_name is given, then starting node will be the first element of the list of nodes.
        Also can be given the index of the starting node in the list of nodes and that 
        will be the starting node.
        Args:
            starting_node_name (str): name of the starting node
            starting_node_index (int): index of the starting node
        Returns:
            Graph: graph with the DFS tree
        """
        starting_node = list(self.nodes)[starting_node_index]
            
        dfs_tree = Graph(name=f"DFS_I_{self.name}")
        visited = set()
        stack = list()
        stack.append(starting_node)
        while stack:
            current_node = stack.pop()
            visited.add(current_node)
            for edge in current_node.get_edges():
                connected_node = edge.get_connected_node(current_node)
                if connected_node not in visited:
                    stack.append(connected_node)
                    dfs_tree.add_edge(current_node, connected_node)
                    visited.add(connected_node)

        return dfs_tree


    def get_dijkstra(self, as_color_tree:bool = True) -> None:
        """
        Calculate the shortest path tree of the graph given an starting node
        The path will be calculated using the Dijkstra algorithm
        and can either mark the tree as a set of edges with color altered
        or as a new Graph with the shortest path tree
        """
        # Create visited nodes list
        visited = set()
        # Create the shortest path tree
        shortest_path_tree = dict()
        set_of_minimun_edges = list()
        
        for node in self.nodes:
            shortest_path_tree[node] = (None, float('inf'))
        
        # Set starting node updating its distance to 0
        shortest_path_tree[list(self.nodes)[0]] = (None, 0)
        
        while len(visited) < len(self.nodes):
            # Get the node with the minimum distance
            current_node = min((node for node in self.nodes if node not in visited), key=lambda x: shortest_path_tree[x][1])
            visited.add(current_node)
            
            for edge in current_node.get_edges():
                connected_node = edge.get_connected_node(current_node)
                if connected_node not in visited:
                    distance = shortest_path_tree[current_node][1] + edge.weigth
                    if distance < shortest_path_tree[connected_node][1]:
                        shortest_path_tree[connected_node] = (current_node, distance)

                        for prev_edge in connected_node.get_edges():
                            prev_edge.alter_color = False
    
                        if edge not in set_of_minimun_edges:
                            set_of_minimun_edges.append(edge)
                            edge.alter_color = True
                        
        
        # Update node name and add sufix to the node name with the distance
        for node in self.nodes:
            node.name = f"{node.name}_{shortest_path_tree[node][1]}"
        # Create a new graph with the shortest path tree
        # shortest_path_tree_graph = Graph(name=f"Only_tree_Dijkstra_{self.name}")
        
        # for edge in set_of_minimun_edges:
        #     shortest_path_tree_graph.add_edge(edge.node_from, edge.node_to, edge.weigth)
        # shortest_path_tree_graph.save_graphviz_with_weigth()
        
    def get_MST_by_kruskal_direct(self) -> None:
        """
        Calculate the minimum spanning tree of the graph given an starting node
        The path will be calculated using the Kruskal algorithm
        """
        # Create visited nodes list
        visited = set()
        # Create the shortest path tree
        set_of_minimun_edges = list()
        # Create the set of sets to keep track of the connected components
        connected_components = set()
        
        for node in self.nodes:
            connected_components.add(frozenset([node]))
        
        # Create a list of edges
        list_of_edges = list(self.edges)
        # Sort the list of edges by weight
        list_of_edges.sort(key=lambda x: x.weigth)
        
        while len(connected_components) > 1 and list_of_edges != []:
            # Get the edge with the minimum weight
            edge = list_of_edges.pop(0)
            # Get the connected nodes of the edge
            node_from, node_to = edge.get_nodes()
            # Get the connected components of the nodes
            component_from = None
            component_to = None
            for component in connected_components:
                if node_from in component:
                    component_from = component
                if node_to in component:
                    component_to = component
            # If the nodes are in different components, add the edge to the minimum spanning tree
            if component_from != component_to:
                set_of_minimun_edges.append(edge)
                connected_components.remove(component_from)
                connected_components.remove(component_to)
                connected_components.add(component_from.union(component_to))
        
        # Create a new graph with the minimum spanning tree
        minimum_spanning_tree = Graph(name=f"MST_Kruskal_{self.name}")
        
        for edge in set_of_minimun_edges:
            minimum_spanning_tree.add_edge(edge.node_from, edge.node_to, edge.weigth)
        # Print value of mst:
        mst_weight = sum([edge.weigth for edge in set_of_minimun_edges])
        print("---------------------------------------")
        print(f"Direct Kruskal MST value: {mst_weight}")
        minimum_spanning_tree.save_graphviz_with_weigth()