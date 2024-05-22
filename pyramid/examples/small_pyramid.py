from pyramid.brick import Brick
from pyramid.node import Node
from pyramid.graph import Graph
from pyramid.helper_functions import counter

small_pyramid = Graph("small_pyramid")

c = counter()
# Create all Nodes in a pyramid
for j in range(3):
    for i in range(3):
        small_pyramid.add_node(Node(16*i, 16*j, 0, next(c)))
for j in range(2):
    for i in range(2):
        small_pyramid.add_node(Node(16*i+8, 16*j+8, 5, next(c)))

small_pyramid.add_node(Node(16, 16, 10, next(c)))


steps = [(8, 8, 5), (-8, 8, 5), (8, -8, 5), (-8, -8, 5),
         (16, 0, 0), (-16, 0, 0), (0, 16, 0), (0, -16, 0),
         (8, 8, -5), (-8, 8, -5), (8, -8, -5), (-8, -8, -5)]

for node_id1 in small_pyramid.nodes:
    for node_id2 in small_pyramid.nodes:
        node1 = small_pyramid.nodes[node_id1]
        node2 = small_pyramid.nodes[node_id2]

        if node1.get_offset(node2) in steps:
            node1.add_neighbor(node2)

small_pyramid_bricks = [[],
          [(16, 0, 0)],
          [(16, 0, 0), (0, 16, 0)],
          [(16, 0, 0), (16, 0, 0), (0, 16, 0)],
          [(16, 0, 0), (0, 16, 0), (-16, 0, 0)]]

c = counter()

small_pyramid_bricks = [Brick(b_d, next(c)) for b_d in small_pyramid_bricks]


if __name__ == "__main__":
    for node_id in small_pyramid:
        node = small_pyramid[node_id]
        print(f"\n{node} has neighbors:")
        for neighbor_id in node.neighbors:
            neighbor = node.neighbors[neighbor_id]
            print("  ", neighbor)

    print("\n\n")
    for brick in small_pyramid_bricks:
        print(brick)
