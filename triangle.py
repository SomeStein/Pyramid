from brick import Brick
from node import Node
from graph import Graph
from helper_functions import counter

c = counter()

triangle = Graph("triangle")

for j in range(10):
    for i in range(j+1):
        triangle.add_node(Node(16*i, 16*j, 0, next(c)))

steps = [(16, 0, 0), (-16, 0, 0), (0, 16, 0), (0, -16, 0)]

for node_id1 in triangle.nodes:
    for node_id2 in triangle.nodes:
        node1 = triangle.nodes[node_id1]
        node2 = triangle.nodes[node_id2]

        if node1.get_offset(node2) in steps:
            node1.add_neighbor(node2)

brick_rosa = [(16, 0, 0), (0, 16, 0)]
brick_blue = [(16, 0, 0), (0, 16, 0), (-16, 0, 0)]
brick_white = [(16, 0, 0), (16, 0, 0), (16, 0, 0)]
brick_red = [(16, 0, 0), (16, 0, 0), (0, 16, 0)]
brick_yellow = [(16, 0, 0), (16, 0, 0), (16, 0, 0), (0, 16, 0)]
brick_lime = [(16, 0, 0), (16, 0, 0), (0, 16, 0), (0, 16, 0)]
brick_grey = [(16, 0, 0), (16, 0, 0), (0, 16, 0), (-16, 0, 0)]
brick_lightblue = [(16, 0, 0), (0, 16, 0), (0, 16, 0), (-16, 0, 0)]
brick_pink = [(16, 0, 0), (16, 0, 0), (0, 16, 0), (16, 0, 0)]
brick_green = [(16, 0, 0), (0, 16, 0), (16, 0, 0), (0, 16, 0)]
brick_orange = [(16, 0, 0), (16, 0, 0), (-16, 0, 0),
                (0, -16, 0), (0, 16, 0), (0, 16, 0)]
brick_violet = [(16, 0, 0), (16, 0, 0), (16, 0, 0), (-16, 0, 0), (0, 16, 0)]


bricks = [brick_orange, brick_blue, brick_white, brick_lime,
          brick_green, brick_lightblue, brick_rosa, brick_yellow,
          brick_violet,  brick_pink, brick_red, brick_grey]

import random 

c = counter()

bricks = [Brick(b_d, next(c)) for b_d in bricks]
