from helper_functions import counter


class Brick:
    def __init__(self, directions: tuple[int], id: int):
        self.directions = directions
        self.id = id

    def __getitem__(self, item: int) -> tuple[int]:
        return self.directions[item]

    def __iter__(self):
        return self.directions.__iter__()

    def __str__(self):
        string = f"Brick {self.id}:" + " "*(6-len(str(self.id))) + "["
        for tup in self:
            a, b, c = tup

            string += "("
            string += " "*(3-len(str(a))) + str(a) + ","
            string += " "*(4-len(str(b))) + str(b) + ","
            string += " "*(4-len(str(c))) + str(c) + "),   "

        string = string[:-4]
        string += "]"

        return string

    def __len__(self):
        return len(self.directions)


def calculate_brick_transforms(brick: Brick, steps: list[tuple[int]]) -> list[Brick]:

    def get_transformer(dir: tuple[int], rot: int) -> dict:
        transf = {}
        transf[(16, 0, 0)] = dir
        transf[(-16, 0, 0)] = tuple([-a for a in dir])
        if rot == 1:
            match dir:
                case (16, 0, 0):
                    transf[(0, 16, 0)] = (0, 16, 0)
                case (-16, 0, 0):
                    transf[(0, 16, 0)] = (0, 16, 0)
                case (0, 16, 0):
                    transf[(0, 16, 0)] = (16, 0, 0)
                case (0, -16, 0):
                    transf[(0, 16, 0)] = (16, 0, 0)
                case (8, 8, 5):
                    transf[(0, 16, 0)] = (-8, -8, 5)
                case (-8, 8, 5):
                    transf[(0, 16, 0)] = (8, -8, 5)
                case (8, -8, 5):
                    transf[(0, 16, 0)] = (-8, 8, 5)
                case (-8, -8, 5):
                    transf[(0, 16, 0)] = (8, 8, 5)
                case (8, 8, -5):
                    transf[(0, 16, 0)] = (-8, -8, -5)
                case (-8, 8, -5):
                    transf[(0, 16, 0)] = (8, -8, -5)
                case (8, -8, -5):
                    transf[(0, 16, 0)] = (-8, 8, -5)
                case (-8, -8, -5):
                    transf[(0, 16, 0)] = (8, 8, -5)
        if rot == 2:
            match dir:
                case (16, 0, 0):
                    transf[(0, 16, 0)] = (0, -16, 0)
                case (-16, 0, 0):
                    transf[(0, 16, 0)] = (0, -16, 0)
                case (0, 16, 0):
                    transf[(0, 16, 0)] = (-16, 0, 0)
                case (0, -16, 0):
                    transf[(0, 16, 0)] = (-16, 0, 0)
                case (8, 8, 5):
                    transf[(0, 16, 0)] = (8, 8, -5)
                case (-8, 8, 5):
                    transf[(0, 16, 0)] = (-8, 8, -5)
                case (8, -8, 5):
                    transf[(0, 16, 0)] = (8, -8, -5)
                case (-8, -8, 5):
                    transf[(0, 16, 0)] = (-8, -8, -5)
                case (8, 8, -5):
                    transf[(0, 16, 0)] = (8, 8, 5)
                case (-8, 8, -5):
                    transf[(0, 16, 0)] = (-8, 8, 5)
                case (8, -8, -5):
                    transf[(0, 16, 0)] = (8, -8, 5)
                case (-8, -8, -5):
                    transf[(0, 16, 0)] = (-8, -8, 5)

        transf[(0, -16, 0)] = tuple([-a for a in transf[(0, 16, 0)]])
        return transf

    def transform(brick: Brick, dir: tuple[int], rot: int, id: int) -> Brick:
        transf = get_transformer(dir, rot)
        new_brick = []
        for step in brick:
            new_brick.append(transf[step])
        new_brick = Brick(new_brick, id)
        return new_brick

    brick_transforms = []

    c = counter()

    for dir in steps:
        for rot in [1, 2]:
            transformed_brick = transform(
                brick, dir, rot, int(str(brick.id*10) + str(next(c))))
            brick_transforms.append(transformed_brick)

    # remove transforms with same footprint
    def get_hitted_points(brick, starting_point=(0, 0, 0)):
        points = [starting_point]
        for tup in brick:
            dx, dy, dz = tup
            x, y, z = points[len(points) - 1]
            points.append((x+dx, y+dy, z+dz))
        return points

    # if there is a pair of not equal transforms but they hit the same cells from (possibly) differnet starting positions one of them can be deleted
    for i in range(len(brick_transforms)-1, -1, -1):
        brick = brick_transforms[i]
        unique = True
        for other_brick in brick_transforms[:i]:
            for starting_point in get_hitted_points(brick):
                if not any(set(get_hitted_points(other_brick, starting_point)) - set(get_hitted_points(brick))):
                    unique = False

        if not unique:
            brick_transforms.pop(i)

    return brick_transforms
