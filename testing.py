from pyramid import get_solutions, get_configurations, render_configuration
from pyramid.examples.small_pyramid import small_pyramid, small_pyramid_bricks
from pyramid.examples.medium_pyramid import medium_pyramid, medium_pyramid_bricks
from pyramid.examples.pyramid import pyramid, pyramid_bricks
from pyramid.examples.small_triangle import small_triangle, small_triangle_bricks
from pyramid.examples.medium_triangle import medium_triangle, medium_triangle_bricks
from pyramid.examples.triangle import triangle, triangle_bricks
import os
import pickle

if __name__ == "__main__":

    get_solutions(small_pyramid, small_pyramid_bricks)
    get_solutions(medium_pyramid, medium_pyramid_bricks)
    get_solutions(pyramid, pyramid_bricks)
    get_solutions(small_triangle, small_triangle_bricks)
    get_solutions(medium_triangle, medium_triangle_bricks)
    # get_solutions(triangle, triangle_bricks) # takes about 15 hours

    file_paths = os.listdir("solves")
    for file_path in file_paths:
        configs = get_configurations("solves/" + file_path)
        print(file_path, len(configs))

    for file_path in file_paths:
        data = False
        with open("solves/" + file_path, "rb") as file:
            data = pickle.load(file)
        graph = data["graph"]
        config = configs[0]
        render_configuration(graph, config)
