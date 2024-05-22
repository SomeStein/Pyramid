
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

def symmetries_filter(graph, order1_sets):
    pass


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
