from generators import algorithms
import argparse


def generate_graph(args):
    type_of_graphs = ["mesh", "erdos", "gilbert", "geo", "barabasi", "dorogo"]
    dict_options = {
        "mesh": algorithms.mesh_random_graph,
        "erdos": algorithms.erdos_renyi_random_graph,
        "gilbert": algorithms.gilbert_random_graph,
        "geo": algorithms.geographical_random_graph,
        "barabasi": algorithms.barabasi_albert_graph,
        "dorogo": algorithms.dorogovtsev_mendes_graph
    }

    if args.type not in type_of_graphs:
        raise ValueError("Type of graph not found")

    if args.type == "mesh":
        if args.m is None or args.n is None:
            raise ValueError("You need to specify the main and secondary number of nodes")
        graph = dict_options[args.type](m=args.m, n=args.n, is_directed=args.directed, graph_name=args.output)

        print("List of nodes: ", graph.nodes)
        print(len(graph.nodes))
        # print("List of edges: ", graph.edges)
    elif args.type == "erdos":
        if args.m is None or args.n is None:
            raise ValueError("You need to specify the main and secondary number of nodes")
        elif args.m < 1 or args.n < 1:
            raise ValueError("m and n must be bigger than 1")
        # elif args.n < args.m - 1:
        #     raise ValueError("m must be bigger than n - 1")
        elif args.directed and args.m > (args.n * (args.n - 1)):
            raise ValueError("m must be smaller than n(n-1)")
        elif not args.directed and args.m > ((args.n * (args.n - 1)) / 2):
            raise ValueError("m must be smaller than n(n-1)/2")

        graph = dict_options[args.type](n=args.n, m=args.m)

        print("List of nodes: ", graph.nodes)
        print(len(graph.nodes))
        print("List of edges: ", graph.edges)

    elif args.type == "gilbert":
        if args.n is None or args.probability is None:
            raise ValueError("You need to specify the main number of nodes (n) and the probability (p)")
        elif args.n < 1 or args.probability < 0 or args.probability > 1:
            raise ValueError("m must be bigger than 1 and probability between 0 and 1")
        graph = dict_options[args.type](n=args.n, p=args.probability, is_directed=args.directed, graph_name=args.output)
        print(f"List of {len(graph.nodes)} nodes: {graph.nodes}")
        print(f"List of {len(graph.edges)} edges:  {graph.edges}")
        
    elif args.type == "geo":
        if args.n is None or args.probability is None:
            raise ValueError("You need to specify the main number of nodes (n) and the radius (r)")
        elif args.n < 1 or args.probability < 0:
            raise ValueError("m must be bigger than 1 and radius must be positive")
        graph = dict_options[args.type](n=args.n, r=args.probability, is_directed=args.directed, graph_name=args.output)
        print(f"List of {len(graph.nodes)} nodes: {graph.nodes}")
        print(f"List of {len(graph.edges)} edges:  {graph.edges}")
        
def main():
    parser = argparse.ArgumentParser(description="Generate a graph by different algorithms")
    parser.add_argument("-t", "--type", type=str, help="Type of graph to generate from the list: mesh, erdos, gilbert, geo, barabasi, dorogo")
    parser.add_argument("-m", type=int, help="Main number of nodes in the ")
    parser.add_argument("-n", type=int, help="Secondary number of nodes in the graph (If algorithm needs it)")
    parser.add_argument("-p", "--probability", type=float, help="Probability of the edge to be created")
    parser.add_argument("-d", "--directed", action=argparse.BooleanOptionalAction, help="If the graph is directed", default=True)
    parser.add_argument("-o", "--output", type=str, help="Output file name", default="")

    args = parser.parse_args()
    generate_graph(args)


if __name__ == "__main__":
    main()

