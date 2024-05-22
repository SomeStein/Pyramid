from pyramid import get_solutions
from pyramid.examples.small_pyramid import small_pyramid, small_pyramid_bricks
from pyramid.examples.medium_pyramid import medium_pyramid, medium_pyramid_bricks
from pyramid.examples.pyramid import pyramid, pyramid_bricks
from pyramid.examples.triangle import triangle, triangle_bricks

if __name__ == "__main__":
   get_solutions(medium_pyramid, medium_pyramid_bricks)
   