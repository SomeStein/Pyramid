from pyramid import get_solutions, get_configurations, render_configuration
from pyramid.examples.small_pyramid import small_pyramid, small_pyramid_bricks
from pyramid.examples.medium_pyramid import medium_pyramid, medium_pyramid_bricks
from pyramid.examples.pyramid import pyramid, pyramid_bricks
from pyramid.examples.triangle import triangle, triangle_bricks
import os

if __name__ == "__main__":

    # file_paths = os.listdir("solves")
    # for file_path in file_paths:
    #     configs = get_configurations("solves/" + file_path)
    #     print(file_path, len(configs))

    # config = get_configurations("solves/pyramid_solutions.data")[0]

    # render_configuration(pyramid, config)

    get_solutions(pyramid, pyramid_bricks)
