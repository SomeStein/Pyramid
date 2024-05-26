
def counter():
    num = 0
    while True:
        num += 1
        yield num


def merge_sets(set1: set[int], set2: set[int]) -> set[int]:
    if set1.isdisjoint(set2):
        return set1.union(set2)
    return False


def get_fraction(sol: list[int], ranges: list[tuple[int]]) -> float:

    lengths = [end - start for start, end in ranges]

    sum = 0

    for k in range(len(sol)):

        prod = 1

        for length in lengths[:k+1]:
            prod *= length

        summand = (sol[k] - ranges[k][0]) / prod
        sum += summand

    return sum


def get_combinations(brick_lists1: list[set[int]], brick_lists2: list[set[int]]) -> list[set[int]]:
    combinations = []
    for set1 in brick_lists1:
        for set2 in brick_lists2:
            merged = merge_sets(set1, set2)
            if merged:
                combinations.append(merged)
    return combinations


def ranges_generator(lengths: list[int], ranges_list: list, num: int, tuple_list: list[tuple[int]] = []) -> list[tuple[int]]:

    if len(tuple_list) > len(lengths):
        print("too many splits")
        raise Exception
    if num <= 1:
        ranges = tuple_list + [(0, l) for l in lengths[len(tuple_list):]]
        ranges_list.append(ranges)
        return

    b = lengths[len(tuple_list)]
    a = int(b/2)

    new_tuple_list_a = tuple_list + [(0, a)]
    new_tuple_list_b = tuple_list + [(a, b)]

    ranges_generator(lengths, ranges_list, num/2,  new_tuple_list_a)
    ranges_generator(lengths, ranges_list, num/2,  new_tuple_list_b)


def rotate_90(id_list, a):
    new_list = []
    for k in range(a):
        for i, id in enumerate(id_list[k*a:(k+1)*a]):
            new_list.insert(i*(k+1), id)
    return new_list


def mirror_x(id_list, a):
    new_list = []
    for k in range(a):
        new_list += id_list[a*(a-k-1):a*(a-k)]
    return new_list


def diag_morror(original_list):

    rows = int(-1/2 + (1/4 + 2*len(original_list))**(1/2))

    triangle = []
    start = 0
    for i in range(rows):
        end = start + i + 1
        triangle.append(original_list[start:end])
        start = end

    diag_tria = []

    for i in range(1, rows+1):
        for j in range(1, i+1):
            e = triangle[rows - j][rows - i]
            diag_tria.append(e)

    return diag_tria


def get_graph_symmetries(graph) -> list[dict]:

    graph_symmetries = []

    if "pyramid" in graph.name:

        heights = list(set([node.z for node in graph.nodes.values()]))
        heights.sort()

        symmetry_dict = {}
        for height in heights:
            id_list = []
            for node in graph.nodes.values():
                if node.z == height:
                    id_list.append(node.id)

            # TRANSFORMATION
            a = int(len(id_list)**(1/2))
            new_id_list = mirror_x(id_list, a)

            for i in range(len(id_list)):
                symmetry_dict[id_list[i]] = new_id_list[i]
        graph_symmetries.append(symmetry_dict)

        symmetry_dict = {}
        for height in heights:
            id_list = []
            for node in graph.nodes.values():
                if node.z == height:
                    id_list.append(node.id)

            # TRANSFORMATION
            a = int(len(id_list)**(1/2))
            new_id_list = rotate_90(id_list, a)

            for i in range(len(id_list)):
                symmetry_dict[id_list[i]] = new_id_list[i]
        graph_symmetries.append(symmetry_dict)

        symmetry_dict = {}
        for height in heights:
            id_list = []
            for node in graph.nodes.values():
                if node.z == height:
                    id_list.append(node.id)

            # TRANSFORMATION
            a = int(len(id_list)**(1/2))
            new_id_list = rotate_90(id_list, a)
            new_id_list = mirror_x(new_id_list, a)

            for i in range(len(id_list)):
                symmetry_dict[id_list[i]] = new_id_list[i]
        graph_symmetries.append(symmetry_dict)

        symmetry_dict = {}
        for height in heights:
            id_list = []
            for node in graph.nodes.values():
                if node.z == height:
                    id_list.append(node.id)

            # TRANSFORMATION
            a = int(len(id_list)**(1/2))
            new_id_list = rotate_90(id_list, a)
            new_id_list = rotate_90(new_id_list, a)

            for i in range(len(id_list)):
                symmetry_dict[id_list[i]] = new_id_list[i]
        graph_symmetries.append(symmetry_dict)

        symmetry_dict = {}
        for height in heights:
            id_list = []
            for node in graph.nodes.values():
                if node.z == height:
                    id_list.append(node.id)

            # TRANSFORMATION
            a = int(len(id_list)**(1/2))
            new_id_list = rotate_90(id_list, a)
            new_id_list = rotate_90(new_id_list, a)
            new_id_list = mirror_x(new_id_list, a)

            for i in range(len(id_list)):
                symmetry_dict[id_list[i]] = new_id_list[i]
        graph_symmetries.append(symmetry_dict)

        symmetry_dict = {}
        for height in heights:
            id_list = []
            for node in graph.nodes.values():
                if node.z == height:
                    id_list.append(node.id)

            # TRANSFORMATION
            a = int(len(id_list)**(1/2))
            new_id_list = rotate_90(id_list, a)
            new_id_list = rotate_90(new_id_list, a)
            new_id_list = rotate_90(new_id_list, a)

            for i in range(len(id_list)):
                symmetry_dict[id_list[i]] = new_id_list[i]
        graph_symmetries.append(symmetry_dict)

        symmetry_dict = {}
        for height in heights:
            id_list = []
            for node in graph.nodes.values():
                if node.z == height:
                    id_list.append(node.id)

            # TRANSFORMATION
            a = int(len(id_list)**(1/2))
            new_id_list = rotate_90(id_list, a)
            new_id_list = rotate_90(new_id_list, a)
            new_id_list = rotate_90(new_id_list, a)
            new_id_list = mirror_x(new_id_list, a)

            for i in range(len(id_list)):
                symmetry_dict[id_list[i]] = new_id_list[i]
        graph_symmetries.append(symmetry_dict)

        return graph_symmetries

    elif "triangle" in graph.name:

        heights = list(set([node.z for node in graph.nodes.values()]))
        heights.sort()

        symmetry_dict = {}
        for height in heights:
            id_list = []
            for node in graph.nodes.values():
                if node.z == height:
                    id_list.append(node.id)

            # TRANSFORMATION
            new_id_list = diag_morror(id_list)

            for i in range(len(id_list)):
                symmetry_dict[id_list[i]] = new_id_list[i]
        graph_symmetries.append(symmetry_dict)

        return graph_symmetries


def symmetry_duplicates(brick_set, brick_sets, graph_symmetries):
    for other_brick_set in brick_sets:
        for symmetry_dict in graph_symmetries:
            transformed_other_brick_set = set()
            for node_id in other_brick_set:
                transformed_node_id = symmetry_dict[node_id]
                transformed_other_brick_set.add(transformed_node_id)
            if brick_set == transformed_other_brick_set:
                return True
    return False


def symmetries_filter(graph, order1_sets):

    graph_symmetries = get_graph_symmetries(graph)

    max_reduction = 0
    max_reduction_index = 0

    for index in range(len(order1_sets)):

        brick1_sets = order1_sets[index].copy()

        for i in range(len(brick1_sets)-1, -1, -1):
            brick1_set = brick1_sets[i]
            if symmetry_duplicates(brick1_set, brick1_sets[:i], graph_symmetries):
                brick1_sets.pop(i)

        if len(order1_sets[index])/len(brick1_sets) > max_reduction:
            max_reduction = len(order1_sets[index])/len(brick1_sets)
            max_reduction_index = index

    brick1_sets = order1_sets[max_reduction_index].copy()

    for i in range(len(brick1_sets)-1, -1, -1):
        brick1_set = brick1_sets[i]
        if symmetry_duplicates(brick1_set, brick1_sets[:i], graph_symmetries):
            brick1_sets.pop(i)

    return order1_sets[:max_reduction_index] + [brick1_sets] + order1_sets[max_reduction_index+1:]


def optimize_brick_order(order1_sets: list[list[set[int]]]) -> tuple[list[int], int]:

    # Pair each sublist with its original index
    indexed_lists = [(i, sublist) for i, sublist in enumerate(order1_sets)]

    # Sort the pairs based on the length of the sublists
    sorted_indexed_lists = sorted(indexed_lists, key=lambda x: len(x[1]))[::-1]

    # Sort the pairs based on the length of the sublists
    sorted_indexed_lists = sorted(
        sorted_indexed_lists, key=lambda x: len(x[1][0]))[::-1]

    # Extract the sorted sublists and the original indices
    sorted_lists = [sublist for _, sublist in sorted_indexed_lists]
    original_indices = [index for index, _ in sorted_indexed_lists]

    return sorted_lists, original_indices
