from generators import algorithms
import argparse


if __name__ == "__main__":
    type_of_graphs = ["mesh", "erdos", "gilbert", "geo", "barabasi", "dorogo"]
    dict_options = {
        "mesh": algorithms.mesh_random_graph,
        "erdos": algorithms.erdos_renyi_random_graph,
        "gilbert": algorithms.gilbert_random_graph,
        "geo": algorithms.geographical_random_graph,
        "barabasi": algorithms.barabasi_albert_graph,
        "dorogo": algorithms.dorogovtsev_mendes_graph
    }
    parser = argparse.ArgumentParser(description="Generate a graph by different algorithms")
    parser.add_argument("-t", "--type", type=str, help="Type of graph to generate from the list: mesh, erdos, gilbert, geo, barabasi, dorogo")
    parser.add_argument("-m", type=int, help="Main number of nodes in the ")
    parser.add_argument("-n", type=int, help="Secondary number of nodes in the graph (If algorithm needs it)")
    parser.add_argument("-d", "--directed", action=argparse.BooleanOptionalAction, help="If the graph is directed", default=True)
    parser.add_argument("-o", "--output", type=str, help="Output file name", default="")
    
    args = parser.parse_args()
    
    if args.type not in type_of_graphs:
        print("Type of graph not found")
        raise ValueError()
    
    if args.type == "mesh":
        if args.m is None or args.n is None:
            print("You need to specify the main and secondary number of nodes")
            raise ValueError()
        graph = dict_options[args.type](m=args.m, n=args.n, is_directed=args.directed, graph_name=args.output)
    
        print("List of nodes: ", graph.nodes)
        print(len(graph.nodes))
        # print("List of edges: ", graph.edges)
    elif args.type == "erdos":
        if args.m is None or args.n is None:
            print("You need to specify the main and secondary number of nodes")
            raise ValueError()
        elif args.m < 1 or args.n < 1:
            print("m and n must be bigger than 1")
            raise ValueError()
        # elif args.n < args.m - 1:
        #     print("m must be bigger than n - 1")
        #     raise ValueError()
        elif args.directed and args.m > (args.n * (args.n - 1)):
            print("m must be smaller than n(n-1)")
            raise ValueError()
        elif not args.directed and args.m > ((args.n * (args.n - 1)) / 2):
            print("m must be smaller than n(n-1)/2")
            raise ValueError()

        graph = dict_options[args.type](n=args.n, m=args.m)

        print("List of nodes: ", graph.nodes)
        print(len(graph.nodes))
        print("List of edges: ", graph.edges)