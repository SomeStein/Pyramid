import pickle
from pyramid.graph import Graph
from pyramid.brick import Brick, calculate_brick_transforms
from pyramid.helper_functions import symmetries_filter, optimize_brick_order, ranges_generator


def preprocessing(graph: Graph, bricks: list[Brick]) -> list[list[set[int]]]:

    # get steps from graph for orientations
    steps = graph.get_all_offsets()

    # calculate all orientations of the bricks
    transformed_bricks = [calculate_brick_transforms(
        brick, steps) for brick in bricks]

    # generate all graph lists with one brick in them

    order1_graph_lists: list[list[list[int]]] = []

    for i in range(len(transformed_bricks)):
        order1_graph_lists.append([])
        for brick in transformed_bricks[i]:
            for node_id in graph:
                check_list = [0]*len(graph)
                if not graph.check_overlap(brick, node_id, check_list):
                    graph.lay(brick, node_id, check_list)
                    check_set = {i for i in range(
                        len(check_list)) if check_list[i]}
                    order1_graph_lists[i].append(check_set)

    return order1_graph_lists


def initialize(graph: Graph, bricks: list[Brick], num_processes: int, queue, total_found) -> list[tuple]:

    print("initializing...\n")

    # Unoptimized preprocessing
    order1_sets = preprocessing(graph, bricks)
    print("1st order list preprocessed\n")
    
    
    # Filter brick with highest reduction by graph symmetries 
    order1_sets = symmetries_filter(graph, order1_sets)
    

    # Optimize brick order
    order1_sets, brick_order = optimize_brick_order(order1_sets)
    if brick_order != list(range(len(order1_sets))):
        print("new brick order: ", brick_order, "\n")
    
        print("optimized 1st order list preprocessed\n")
        

    # Numbers of unique brick configuratons
    string = "order 1 counts for optimized brick order:  "
    for brick_lists in order1_sets:
        string += str(len(brick_lists)) + ", "
    string = string[:-2]
    print(string, "\n")
    

    # File managing
    file_path = f'solves/{graph.name}_solutions.data'
    print("Checking for solutions in", file_path, "\n")

    try:
        with open(file_path, "rb") as file:
            data = pickle.load(file)
            data["graph"]
            data["bricks"]
            data["order1_sets"]
            data["solutions"]

        print("data file exists\n")

    except (FileNotFoundError, KeyError, ModuleNotFoundError):

        print("creating data file\n")

        with open(file_path, 'wb') as file:

            data = {"graph": graph,
                    "bricks": bricks,
                    "order1_sets": order1_sets,
                    "solutions": []}

            pickle.dump(data, file)

    else:
        if data["order1_sets"] != order1_sets:

            import random
            rn = random.randint(0, 1000)
            file_path = f'solves/{graph.name}_solutions({rn}).data'

            print("data does not match, creating new data file at", file_path, "\n")

            with open(file_path, 'wb') as file:
                data = {"graph": graph,
                        "bricks": bricks,
                        "order1_sets": order1_sets,
                        "solutions": []}

                pickle.dump(data, file)
        
        
    # Creating argument list
    argument_list = []
        
        
    # index ranges for bricks for each process
    lengths = [len(l) for l in order1_sets]
    ranges_list = []
    ranges_generator(lengths, ranges_list, num_processes)


    # Task id, manager stuff, brick set lists, ranges 
    for i in range(num_processes):
        tup = (i, queue, total_found, file_path, order1_sets, ranges_list[i])
        argument_list.append(tup)
        print(f"Process {i} has ranges", ranges_list[i])


    # argument list finished
    print("\nreturning argument_list of length:", len(argument_list), "\n")
    return argument_list
