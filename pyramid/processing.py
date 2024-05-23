
from pyramid.helper_functions import get_fraction, merge_sets


def process_solutions(task_id: int, queue, total_found, file_path: str, order1_sets: list[list[set[int]]], ranges: list[tuple[int]], check_set: set[int] = set(), sol: list[int] = []) -> None:

    try:

        len_sol = len(sol)

        if len_sol == len(ranges):

            queue.put((file_path, sol))

            message = f"Process {task_id+1} found: {sol}"

            tot_msg = " "*(90-len(message)) + \
                "total found: " + str(total_found.value)

            print("\n\033[K\n\033[K" + message + tot_msg +
                  "\033[F\033[F\r", end="")

            return

        if len_sol == len(ranges) - 1:

            queue.put((task_id, get_fraction(sol, ranges)))

        start, end = ranges[len_sol]

        for i, brick_set in enumerate(order1_sets[len_sol][start:end]):
            merged = merge_sets(brick_set, check_set)
            if merged:
                process_solutions(task_id, queue, total_found, file_path,
                                  order1_sets, ranges, merged, sol + [start+i])

        if len_sol == 0:

            queue.put((task_id, 1))

    except Exception as e:
        queue.put([task_id, e])
