from pyramid import get_solutions, get_configurations, render_configuration
from pyramid.examples.small_pyramid import small_pyramid, small_pyramid_bricks
from pyramid.examples.medium_pyramid import medium_pyramid, medium_pyramid_bricks
from pyramid.examples.pyramid import pyramid, pyramid_bricks
from pyramid.examples.triangle import triangle, triangle_bricks

if __name__ == "__main__":

    get_solutions(small_pyramid, small_pyramid_bricks)
    get_solutions(medium_pyramid, medium_pyramid_bricks)
    get_solutions(pyramid, pyramid_bricks)

    conf = get_configurations("solves/small_pyramid_solutions.data")[0]
    render_configuration(small_pyramid, conf)

    conf = get_configurations("solves/medium_pyramid_solutions.data")[0]
    render_configuration(medium_pyramid, conf)

    conf = get_configurations("solves/pyramid_solutions.data")[0]
    render_configuration(pyramid, conf)
