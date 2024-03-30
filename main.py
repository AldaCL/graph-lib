from generators import algorithms
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a mesh random graph")
    
    
    graph = algorithms.mesh_random_graph(m=4, n=3)
    print("List of nodes: ", graph.nodes)
    print("List of edges: ", graph.edges)
    