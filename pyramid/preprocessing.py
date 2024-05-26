import pickle
from pyramid.graph import Graph
from pyramid.brick import Brick, calculate_brick_transforms
from pyramid.helper_functions import symmetries_filter, optimize_brick_order, ranges_generator, get_combinations


def preprocessing(graph: Graph, bricks: list[Brick]) -> list[list[set[int]]]:

    # get steps from graph for orientations
    steps = graph.get_all_offsets()

    # calculate all orientations of the bricks
    transformed_bricks = [calculate_brick_transforms(
        brick, steps) for brick in bricks]

    # generate all graph sets with one brick in them

    order1_sets: list[list[set[int]]] = []

    for i in range(len(transformed_bricks)):
        order1_sets.append([])
        for brick in transformed_bricks[i]:
            for node_id in graph:
                check_dict = {}
                if not graph.check_overlap(brick, node_id, check_dict):
                    graph.lay(brick, node_id, check_dict)
                    check_set = set(check_dict.keys())
                    order1_sets[i].append(check_set)

    return order1_sets


def initialize(graph: Graph, bricks: list[Brick], num_processes: int, queue, total_found) -> list[tuple]:

    print("initializing...\n")

    # Unoptimized preprocessing
    order1_sets = preprocessing(graph, bricks)
    print("1st order list preprocessed\n")

    unit_check_sets = [get_combinations(
        order1_sets[2*i], order1_sets[2*i+1]) for i in range(int(len(order1_sets)/4))] + [order1_sets[i] for i in range(int(len(order1_sets)/2), len(order1_sets))]

    # unit_check_sets = order1_sets

    # Filter brick with highest reduction by graph symmetries
    unit_check_sets = symmetries_filter(graph, unit_check_sets)

    # Optimize brick order
    unit_check_sets, brick_order = optimize_brick_order(unit_check_sets)
    if brick_order != list(range(len(unit_check_sets))):
        print("new brick order: ", brick_order, "\n")
        print("optimized 1st order list preprocessed\n")

    bricks = [bricks[i] for i in brick_order]

    # Numbers of unique brick configuratons
    string = "order 1 counts for optimized brick order:  "
    for brick_lists in unit_check_sets:
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
            data["unit_check_sets"]
            data["solutions"]

        print("data file exists\n")

    except (FileNotFoundError, KeyError, ModuleNotFoundError):

        print("creating data file\n")

        with open(file_path, 'wb') as file:

            data = {"graph": graph,
                    "bricks": bricks,
                    "unit_check_sets": unit_check_sets,
                    "solutions": []}

            pickle.dump(data, file)

    else:
        if data["unit_check_sets"] != unit_check_sets or data["bricks"] != bricks:

            import random
            rn = random.randint(0, 1000)
            file_path = f'solves/{graph.name}_solutions({rn}).data'

            print("data does not match, creating new data file at", file_path, "\n")

            with open(file_path, 'wb') as file:
                data = {"graph": graph,
                        "bricks": bricks,
                        "unit_check_sets": unit_check_sets,
                        "solutions": []}

                pickle.dump(data, file)

    # Creating argument list
    argument_list = []

    # index ranges for bricks for each process
    lengths = [len(l) for l in unit_check_sets]
    ranges = []
    ranges_generator(lengths, ranges, num_processes)

    # Task id, manager stuff, brick set lists, ranges
    for i in range(num_processes):
        tup = (i, queue, total_found, file_path,
               unit_check_sets, ranges[i])
        argument_list.append(tup)
        print(f"Process {i} has ranges", ranges[i])

    # argument list finished
    print("\nreturning argument_list of length:", len(argument_list), "\n")
    return argument_list
