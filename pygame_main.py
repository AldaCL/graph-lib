"""
Pygame structure to generate a graph visualization of the data
"""
import pygame
import math
import time
from generators import local_generator
from models.graph import Graph, Node, Edge, GeoNode

def spring_graph_forces_calculation(graph: Graph) -> Graph:
    # Update each node position based on the forces of the spring
    # c1 and c2 are constants that can be adjusted to change the behavior of the spring
    
    # Calculate the forces of the spring
    for node in graph.nodes:
        edges_connected = node.get_edges()
        for edge in edges_connected:
            # Calculate the distance between the nodes
            connected_node = edge.get_connected_node(node)
            distance = node.calculate_distance(connected_node)
            # Calculate the force of the spring
            force = logaritmic_force(distance)
            # Calculate the force in x and y
            force_x = force * (connected_node.x_coord - node.x_coord)/distance
            force_y = force * (connected_node.y_coord - node.y_coord)/distance
            # Update the position of the nodes
            node.x_coord += force_x
            node.y_coord += force_y
            connected_node.x_coord -= force_x
            connected_node.y_coord -= force_y
    return graph

def logaritmic_force(distance: int, c1: float = 0.4, c2: float = 0.1) -> float:
    # Calculate the force of the spring
    return c1 * math.log10(distance/c2)

def draw_initial_graph(graph: Graph) -> Graph:
    n_nodes = len(graph.nodes)
    matrix_size = int(n_nodes ** 0.5)
    step_width = 1280 // matrix_size
    step_height = 720 // matrix_size

    # nodes are a set, so iterate over them
    for i, node in enumerate(graph.nodes):
        x = i % matrix_size
        y = i // matrix_size
        x = x * step_width + step_width // 2
        y = y * step_height + step_height // 2
        node.x_coord = x
        node.y_coord = y

    return graph

def main():
    graph = local_generator.generate_graph_for_all_files_in_folder()[0]
    pygame.init()
    
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    # Set name of window
    pygame.display.set_caption(f"Graph Visualization of {graph.name}")
    graph = draw_initial_graph(graph)
    iterations = 0
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        #If more than 200 iterations, slow the screen
        iterations += 1
        if iterations > 100:
            time.sleep(10)
            running = False
        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")
        # Render 10 s initial position of graph:
        # for edge in graph.edges:
        #     pygame.draw.line(screen, "white", (edge.node_from.x_coord, edge.node_from.y_coord), (edge.node_to.x_coord, edge.node_to.y_coord), 2)
        #     # Draw the nodes
        #     pygame.draw.circle(screen, "red", (edge.node_from.x_coord, edge.node_from.y_coord), 5)
        #     pygame.draw.circle(screen, "red", (edge.node_to.x_coord, edge.node_to.y_coord), 5)
        # # RENDER YOUR GAME HERE
        
        # Update position of nodes and edges based on forces of spring
        # flip() the display to put your work on screen
        # Draw the graph with the new positions and add a delay to see animation
        for edge in graph.edges:
            pygame.draw.line(screen, "white", (edge.node_from.x_coord, edge.node_from.y_coord), (edge.node_to.x_coord, edge.node_to.y_coord), 2)
            # Draw the nodes
            pygame.draw.circle(screen, "red", (edge.node_from.x_coord, edge.node_from.y_coord), 5)
            pygame.draw.circle(screen, "red", (edge.node_to.x_coord, edge.node_to.y_coord), 5)
        
        # sleep 0.2 s to see Animation of the graph
        time.sleep(0.1)
        pygame.display.flip()
        # Slow execution to see the animation
        graph = spring_graph_forces_calculation(graph)
        clock.tick(60)  # limits FPS to 60
        
    pygame.quit()

if __name__ == "__main__":
    main()