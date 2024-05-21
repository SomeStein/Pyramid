
class Node:
    def __init__(self, x, y, z, id):
        self.x = x
        self.y = y
        self.z = z
        self.pos = (x, y, z)
        self.id = id
        self.neighbors = {}

    def __str__(self):
        return f"Node {self.id}: " + str(self.pos)

    def get_offset(self, cell):
        return (cell.x-self.x, cell.y-self.y, cell.z-self.z)

    def add_neighbor(self, cell):
        offset = self.get_offset(cell)
        self.neighbors[offset] = cell
