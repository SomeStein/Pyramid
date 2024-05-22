
from brick import Brick
from node import Node
from graph import Graph
from helper_functions import counter

pyramid = Graph("pyramid")

c = counter()
# Create all Nodes in a pyramid
for j in range(5):
    for i in range(5):
        pyramid.add_node(Node(16*i, 16*j, 0, next(c)))
for j in range(4):
    for i in range(4):
        pyramid.add_node(Node(16*i+8, 16*j+8, 5, next(c)))
for j in range(3):
    for i in range(3):
        pyramid.add_node(Node(16*i+16, 16*j+16, 10, next(c)))
for j in range(2):
    for i in range(2):
        pyramid.add_node(Node(16*i+24, 16*j+24, 15, next(c)))
for j in range(1):
    for i in range(1):
        pyramid.add_node(Node(16*i+32, 16*j+32, 20, next(c)))


steps = [(8, 8, 5), (-8, 8, 5), (8, -8, 5), (-8, -8, 5),
         (16, 0, 0), (-16, 0, 0), (0, 16, 0), (0, -16, 0),
         (8, 8, -5), (-8, 8, -5), (8, -8, -5), (-8, -8, -5)]

for node_id1 in pyramid.nodes:
    for node_id2 in pyramid.nodes:
        node1 = pyramid.nodes[node_id1]
        node2 = pyramid.nodes[node_id2]

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


pyramid_bricks = [brick_orange, brick_white, brick_blue, brick_lime,
          brick_green, brick_yellow, brick_lightblue, brick_violet,
          brick_pink, brick_rosa, brick_red, brick_grey]

c = counter()

pyramid_bricks = [Brick(b_d, next(c)) for b_d in pyramid_bricks]


if __name__ == "__main__":
    for node_id in pyramid:
        node = pyramid[node_id]
        print(f"\n{node} has neighbors:")
        for neighbor_id in node.neighbors:
            neighbor = node.neighbors[neighbor_id]
            print("  ", neighbor)

    print("\n\n")
    for brick in pyramid_bricks:
        print(brick)
