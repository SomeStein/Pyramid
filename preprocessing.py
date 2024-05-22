import pickle
from graph import Graph
from brick import Brick
from brick import calculate_brick_transforms


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
            for node_id in range(1, len(graph)+1):
                check_list = [0]*len(graph)
                if not graph.check_overlap(brick, node_id, check_list):
                    graph.lay(brick, node_id, check_list)
                    check_set = {i for i in range(
                        len(check_list)) if check_list[i]}
                    order1_graph_lists[i].append(check_set)

    return order1_graph_lists
 
def initialize(graph:Graph, bricks:list[Brick], num_processes:int, queue) -> list[tuple]:
    
    print("initializing...\n")

    # Unoptimized preprocessing
    order1_sets = preprocessing(graph, bricks)
    print("1st order list preprocessed\n")
    print("optimizing brick order by pair merging\n")
    
    # Optimize brick order
    # brick_order, min = optimize_brick_order(order1_sets)
    # print("new brick order: ", brick_order, "with prod", min, "\n")
    brick_order = list(range(len(bricks)))
    bricks = [bricks[i] for i in brick_order]
    from random import shuffle
    #shuffle(bricks)
    
    # Optimized preprocessing
    order1_sets = preprocessing(graph, bricks)
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

    except (FileNotFoundError,KeyError):

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
                
                
    
    
    
    def ranges_generator(lengths:list[int], ranges_list:list, num:int, tuple_list:list[tuple[int]]=[]) -> list[tuple[int]]:
        
        if len(tuple_list) > len(lengths):
            print("too many splits")
            raise Exception
        if num <= 1:
            ranges = tuple_list + [(0,l) for l in lengths[len(tuple_list):]]
            ranges_list.append(ranges)
            return
        
        b = lengths[len(tuple_list)]
        a = int(b/2)
        
        new_tuple_list_a = tuple_list + [(0, a)]
        new_tuple_list_b = tuple_list + [(a, b)]
        
        ranges_generator(lengths, ranges_list, num/2,  new_tuple_list_a) 
        ranges_generator(lengths, ranges_list, num/2,  new_tuple_list_b) 
        
        
    lengths = [len(l) for l in order1_sets]
    
    ranges_list = []
        
    ranges_generator(lengths, ranges_list, num_processes)
        
    
    argument_list = []

    for i in range(num_processes):

        tup = (i, queue, file_path, order1_sets, ranges_list[i])
        argument_list.append(tup)
        
        print(f"Process {i+1} has ranges", ranges_list[i])
        
    print("\nreturning argument_list of length:", len(argument_list), "\n")

    return argument_list