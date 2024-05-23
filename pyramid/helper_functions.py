
def counter():
    num = 0
    while True:
        num += 1
        yield num


def merge_sets(set1: set[int], set2: set[int]) -> set[int]:
    for e in set1:
        if e in set2:
            return False
    return set1.union(set2)


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


def symmetry_duplicates(brick_set, brick_sets, graph_symmetries):
    for other_brick_set in brick_sets:
        for symmetry_dict in graph_symmetries:
            transformed_other_brick_set = set()
            for node_id in other_brick_set:
                transformed_node_id = symmetry_dict[node_id+1]-1
                transformed_other_brick_set.add(transformed_node_id)
            if brick_set == transformed_other_brick_set:
                return True
    return False


def symmetries_filter(graph, order1_sets):

    graph_symmetries = get_graph_symmetries(graph)

    index = 5

    brick1_sets = order1_sets[index]

    for i in range(len(brick1_sets)-1, -1, -1):
        brick1_set = brick1_sets[i]
        if symmetry_duplicates(brick1_set, brick1_sets[:i], graph_symmetries):
            brick1_sets.pop(i)

    return [brick1_sets] + order1_sets[:index] + order1_sets[index+1:]


def optimize_brick_order(order1_sets: list[list[set[int]]]) -> tuple[list[int], int]:

    min = False
    min_comb = False

    length_dict = {}

    for i in range(len(order1_sets)):
        for j in range(i+1, len(order1_sets)):
            lists1 = order1_sets[i]
            lists2 = order1_sets[j]

            length_dict[(i, j)] = len(get_combinations(lists1, lists2))

    def iter(indices: list[int], pairs: list[tuple[int]] = [], prod=1) -> None:

        nonlocal length_dict
        nonlocal min
        nonlocal min_comb

        if len(indices) == 2:

            prod *= length_dict[(indices[0], indices[1])]

            pairs.append((indices[0], indices[1]))

            if not min:
                min = prod
                min_comb = pairs
                print(pairs, min, end="\r")

            if prod < min:
                min = prod
                min_comb = pairs
                print(pairs, min, end="\r")

            return

        for i in range(len(indices)):
            for j in range(i+1, len(indices)):

                _indices = indices.copy()

                pair = (_indices.pop(i), _indices.pop(j-1))

                l = length_dict[pair]

                _pairs = pairs.copy()
                _pairs.append(pair)

                iter(_indices, _pairs, prod*l)
        return

    iter(list(range(len(order1_sets))))

    brick_order = []

    for i, j in min_comb:
        brick_order.append(i)
        brick_order.append(j)

    return brick_order, min
