import random
from pyramid.brick import Brick
from pyramid.node import Node
from pyramid.graph import Graph
from pyramid.helper_functions import counter

c = counter()

small_triangle = Graph("small_triangle")

for j in range(8):
    for i in range(j+1):
        small_triangle.add_node(Node(16*i, 16*j, 0, next(c)))

steps = [(16, 0, 0), (-16, 0, 0), (0, 16, 0), (0, -16, 0)]

for node_id1 in small_triangle.nodes:
    for node_id2 in small_triangle.nodes:
        node1 = small_triangle.nodes[node_id1]
        node2 = small_triangle.nodes[node_id2]

        if node1.get_offset(node2) in steps:
            node1.add_neighbor(node2)

brick_rosa = [(16, 0, 0), (0, 16, 0)]
brick_blue = [(16, 0, 0), (0, 16, 0), (-16, 0, 0)]
brick_red = [(16, 0, 0), (16, 0, 0), (0, 16, 0)]
brick_yellow = [(16, 0, 0), (16, 0, 0), (16, 0, 0), (0, 16, 0)]
brick_lime = [(16, 0, 0), (16, 0, 0), (0, 16, 0), (0, 16, 0)]
brick_grey = [(16, 0, 0), (16, 0, 0), (0, 16, 0), (-16, 0, 0)]
brick_pink = [(16, 0, 0), (16, 0, 0), (0, 16, 0), (16, 0, 0)]
brick_orange = [(16, 0, 0), (16, 0, 0), (-16, 0, 0),
                (0, -16, 0), (0, 16, 0), (0, 16, 0)]


small_triangle_bricks = [brick_orange, brick_blue, brick_lime,
                         brick_rosa, brick_yellow,
                         brick_pink, brick_red, brick_grey]


c = counter()

small_triangle_bricks = [Brick(b_d, next(c)) for b_d in small_triangle_bricks]
