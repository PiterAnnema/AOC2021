from operator import __sub__, __mul__
from functools import reduce


class Node:
    def __init__(self, height: int) -> None:
        self.height = height
        self.neighbors = set()

    def add_neighbor(self, other):
        self.neighbors.add(other)
        other.neighbors.add(self)

    def __lt__(self, other):
        return self.height.__lt__(other.height)

    def is_local_min(self):
        return all(map(self.__lt__, self.neighbors))

    def get_basin(self):
        check_heap = {self}
        checked = set()
        while check_heap:
            node = check_heap.pop()
            checked.add(node)

            if node.height < 9:
                check_heap |= node.neighbors - checked
                yield node


def read_heightmap():
    nodes = dict()
    with open('data/day9') as f:
        for i, line in enumerate(f):
            for j, height in enumerate(map(int, line.strip())):
                node = Node(height)
                nodes[i, j] = node
                if i > 0:
                    node.add_neighbor(nodes[(i - 1, j)])

                if j > 0:
                    node.add_neighbor(nodes[(i, j - 1)])

    return list(nodes.values())


def main() -> None:
    nodes = read_heightmap()
    minima = list(filter(Node.is_local_min, nodes))

    # Part One
    assert sum(node.height for node in minima) + len(minima) == 575

    # Part Two
    sorted_basins = sorted((len(list(node.get_basin()))
                           for node in minima), reverse=True)
    assert reduce(__mul__, sorted_basins[:3]) == 1019700


if __name__ == '__main__':
    main()
