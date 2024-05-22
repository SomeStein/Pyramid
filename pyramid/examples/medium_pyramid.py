from pyramid.brick import Brick
from pyramid.node import Node
from pyramid.graph import Graph
from pyramid.helper_functions import counter

medium_pyramid = Graph("medium_pyramid")

c = counter()
# Create all Nodes in a pyramid
for j in range(4):
    for i in range(4):
        medium_pyramid.add_node(Node(16*i, 16*j, 0, next(c)))
for j in range(3):
    for i in range(3):
        medium_pyramid.add_node(Node(16*i+8, 16*j+8, 5, next(c)))
for j in range(2):
    for i in range(2):
        medium_pyramid.add_node(Node(16*i+16, 16*j+16, 10, next(c)))
for j in range(1):
    for i in range(1):
        medium_pyramid.add_node(Node(16*i+24, 16*j+24, 15, next(c)))


steps = [(8, 8, 5), (-8, 8, 5), (8, -8, 5), (-8, -8, 5),
         (16, 0, 0), (-16, 0, 0), (0, 16, 0), (0, -16, 0),
         (8, 8, -5), (-8, 8, -5), (8, -8, -5), (-8, -8, -5)]

for node_id1 in medium_pyramid.nodes:
    for node_id2 in medium_pyramid.nodes:
        node1 = medium_pyramid.nodes[node_id1]
        node2 = medium_pyramid.nodes[node_id2]

        if node1.get_offset(node2) in steps:
            node1.add_neighbor(node2)

brick_rosa = [(16, 0, 0), (0, 16, 0)]
brick_blue = [(16, 0, 0), (0, 16, 0), (-16, 0, 0)]
brick_white = [(16, 0, 0), (16, 0, 0), (16, 0, 0)]
brick_red = [(16, 0, 0), (16, 0, 0), (0, 16, 0)]
brick_yellow = [(16, 0, 0), (16, 0, 0), (16, 0, 0), (0, 16, 0)]
brick_lime = [(16, 0, 0), (16, 0, 0), (0, 16, 0), (0, 16, 0)]
brick_grey = [(16, 0, 0), (16, 0, 0), (0, 16, 0), (-16, 0, 0)]
#brick_lightblue = [(16, 0, 0), (0, 16, 0), (0, 16, 0), (-16, 0, 0)]
#brick_pink = [(16, 0, 0), (16, 0, 0), (0, 16, 0), (16, 0, 0)]
#brick_green = [(16, 0, 0), (0, 16, 0), (16, 0, 0), (0, 16, 0)]
#brick_orange = [(16, 0, 0), (16, 0, 0), (-16, 0, 0),
#                (0, -16, 0), (0, 16, 0), (0, 16, 0)]
#brick_violet = [(16, 0, 0), (16, 0, 0), (16, 0, 0), (-16, 0, 0), (0, 16, 0)]


medium_pyramid_bricks = [brick_white, brick_blue, brick_lime,brick_yellow,brick_rosa, brick_red, brick_grey]

c = counter()

medium_pyramid_bricks = [Brick(b_d, next(c)) for b_d in medium_pyramid_bricks]


if __name__ == "__main__":
    for node_id in medium_pyramid:
        node = medium_pyramid[node_id]
        print(f"\n{node} has neighbors:")
        for neighbor_id in node.neighbors:
            neighbor = node.neighbors[neighbor_id]
            print("  ", neighbor)

    print("\n\n")
    for brick in medium_pyramid_bricks:
        print(brick)