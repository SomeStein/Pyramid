from brick import Brick
from node import Node
from graph import Graph
from helper_functions import counter

pyramid = Graph("small_pyramid")

c = counter()
# Create all Nodes in a pyramid
for j in range(3):
    for i in range(3):
        pyramid.add_node(Node(16*i, 16*j, 0, next(c)))
for j in range(2):
    for i in range(2):
        pyramid.add_node(Node(16*i+8, 16*j+8, 5, next(c)))

pyramid.add_node(Node(16, 16, 10, next(c)))


steps = [(8, 8, 5), (-8, 8, 5), (8, -8, 5), (-8, -8, 5),
         (16, 0, 0), (-16, 0, 0), (0, 16, 0), (0, -16, 0),
         (8, 8, -5), (-8, 8, -5), (8, -8, -5), (-8, -8, -5)]

for node_id1 in pyramid.nodes:
    for node_id2 in pyramid.nodes:
        node1 = pyramid.nodes[node_id1]
        node2 = pyramid.nodes[node_id2]

        if node1.get_offset(node2) in steps:
            node1.add_neighbor(node2)

bricks = [[],
          [(16, 0, 0)],
          [(16, 0, 0), (0, 16, 0)],
          [(16, 0, 0), (16, 0, 0), (0, 16, 0)],
          [(16, 0, 0), (0, 16, 0), (-16, 0, 0)]]

c = counter()

bricks = [Brick(b_d, next(c)) for b_d in bricks]


if __name__ == "__main__":
    for node_id in pyramid:
        node = pyramid[node_id]
        print(f"\n{node} has neighbors:")
        for neighbor_id in node.neighbors:
            neighbor = node.neighbors[neighbor_id]
            print("  ", neighbor)

    print("\n\n")
    for brick in bricks:
        print(brick)
