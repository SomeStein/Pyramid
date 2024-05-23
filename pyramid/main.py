from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import time
import os
import pickle
from multiprocessing import Pool, Manager
from rich.progress import Progress, TextColumn, BarColumn, TimeElapsedColumn
from pyramid.graph import Graph
from pyramid.brick import Brick
from pyramid.processing import process_solutions
from pyramid.preprocessing import initialize

# node_id mess
# automatically optimize brick order (maximize blocking with symmetry filter and ordering)
# symmetry for triangle
# symmetry for every graph


def get_solutions(graph: Graph, bricks: list[Brick], num_processes: int = os.cpu_count()) -> None:

    start_time = time.time()

    folder_name = "solves"

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    with Manager() as manager:

        queue = manager.Queue()
        total_found = manager.Value('i', 0, lock=False)
        argument_list = initialize(
            graph, bricks, num_processes, queue, total_found)

        with Progress(
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            "[progress.percentage]{task.percentage:>3.0f}%",
            TimeElapsedColumn(),
        ) as progress:

            task_progress = {}

            for task_id in range(num_processes):

                task_description = f"Process {task_id + 1}"
                task_progress[task_id] = progress.add_task(
                    task_description, total=1)

            with Pool(num_processes) as pool:

                results = []

                for i in range(len(argument_list)):
                    result = pool.apply_async(
                        process_solutions, argument_list[i])
                    results.append(result)

                while any(not progress.tasks[task_id].finished for task_id in task_progress):

                    while not queue.empty():
                        queue_element = queue.get()

                        if type(queue_element) == tuple:

                            if type(queue_element[0]) == int:

                                task_id, progress_amount = queue_element
                                progress.update(
                                    task_progress[task_id], completed=progress_amount)

                            elif type(queue_element[0]) == str:

                                file_path, sol = queue_element

                                global_solutions = []

                                with open(file_path, 'rb') as file:
                                    data = pickle.load(file)
                                    global_solutions = data["solutions"]

                                if sol not in global_solutions:
                                    global_solutions.append(sol)

                                data["solutions"] = global_solutions

                                total_found.value = len(global_solutions)

                                with open(file_path, 'wb') as file:
                                    pickle.dump(data, file)

                        else:
                            print(
                                "Process", queue_element[0]+1, "had an exception:")
                            raise queue_element[1]

        print(f"\n\n\nFinished with {total_found.value} solutions\n")

    print("Took:", round((time.time() - start_time)/60, 2), "min\n")


def get_configurations(file_path):

    with open(file_path, "rb") as file:
        data: dict = pickle.load(file)
        graph: Graph = data["graph"]
        bricks: list[Brick] = data["bricks"]
        order1_sets: list[list[set[int]]] = data["order1_sets"]
        solutions: list[list[int]] = data["solutions"]

    configurations = []

    for sol in solutions:
        configuration = {}
        for i, index in enumerate(sol):
            for node_id in order1_sets[i][index]:
                configuration[node_id+1] = bricks[i].id
        configurations.append(configuration)

    return configurations


def render_configuration(graph: Graph, configuration: dict[int, int]):

    colormap = {
        0: 'red',
        1: 'green',
        2: 'blue',
        3: 'yellow',
        4: 'cyan',
        5: 'magenta',
        6: 'orange',
        7: 'purple',
        8: 'brown',
        9: 'pink',
        10: 'gray',
        11: 'olive',
        12: 'navy'
    }

    colors = []
    x_coords = []
    y_coords = []
    z_coords = []

    for node_id in configuration:
        colors.append(colormap[configuration[node_id]])
        x_coords.append(graph[node_id].x)
        y_coords.append(graph[node_id].y)
        z_coords.append(graph[node_id].z)

    # Create a 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    steps = graph.get_all_offsets()

    # Draw lines between nodes of the same color within valid steps
    for node_id1 in graph:
        for node_id2 in graph:
            if configuration[node_id1] == configuration[node_id2]:
                if graph[node_id1].get_offset(graph[node_id2]) in steps:
                    pos1 = graph[node_id1].pos
                    pos2 = graph[node_id2].pos
                    ax.plot([pos1[0], pos2[0]], [pos1[1], pos2[1]], [
                            pos1[2], pos2[2]], color=colormap[configuration[node_id1]])

    # Scatter plot with colors
    ax.scatter(x_coords, y_coords, z_coords, c=colors, marker='o', s=100)
    ax.set_axis_off()

    plt.show()
