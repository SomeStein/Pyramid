from pyramid.brick import Brick
from pyramid.node import Node


class Graph():
    def __init__(self, name: str):
        self.name = name
        self.nodes: dict[int, Node] = {}

    def __str__(self):
        string = ""
        for node_id in self.nodes:
            string += "\n" + str(self.nodes[node_id])
        return string

    def __iter__(self):
        return self.nodes.__iter__()

    def __getitem__(self, item):
        return self.nodes[item]

    def __len__(self):
        return len(self.nodes)

    def add_node(self, node):
        self.nodes[node.id] = node

    def get_all_offsets(self) -> list[tuple[int]]:
        steps = []
        for node1 in self.nodes.values():
            for node2 in node1.neighbors.values():
                steps.append(node1.get_offset(node2))

        return list(set(steps))

    def get_all_hitted_node_ids(self, brick, node_id):
        nodeIds = []
        node = self.nodes[node_id]
        for i in range(len(brick)):
            node = node.neighbors[brick[i]]
            nodeIds.append(node.id)
        return nodeIds

    def check_overlap(self, brick: Brick, node_id: int, check_list: list[int]) -> list[int]:
        node = self.nodes[node_id]
        if check_list[node.id - 1]:
            return check_list[node.id - 1]
        for i in range(len(brick)):
            try:
                node = node.neighbors[brick[i]]
            except KeyError:
                return True
            if check_list[node.id-1]:
                return node.id
        return False

    def lay(self, brick: Brick, node_id: int, check_list: list[int]) -> None:
        node = self.nodes[node_id]
        check_list[node.id - 1] = brick.id  # "x" + str(brick.id)
        for i in range(len(brick)):
            node = node.neighbors[brick[i]]
            if check_list[node.id-1] != 0 and check_list[node.id-1] != brick.id:
                print(brick.id)
            check_list[node.id-1] = brick.id
