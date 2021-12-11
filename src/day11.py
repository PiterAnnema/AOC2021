from itertools import islice, takewhile


class Octopus:
    def __init__(self, energy: int) -> None:
        self.energy = energy
        self.neighbors = set()

    def increment(self):
        self.energy += 1
        if self.energy == 10:
            self.flash()

    def flash(self):
        for neighbor in self.neighbors:
            neighbor.increment()

    def add_neighbor(self, neighbor):
        self.neighbors.add(neighbor)
        neighbor.neighbors.add(self)


def read_octopi():
    octopi = dict()
    with open('data/day11') as f:
        for i, line in enumerate(f):
            energies = list(map(int, line.strip()))
            for j, energy in enumerate(energies):
                pos = (i, j)
                octopus = Octopus(energy)
                octopi[pos] = octopus
                for nb_pos in octopi.keys() & {(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1)}:
                    octopus.add_neighbor(octopi[nb_pos])

    return list(octopi.values())


def step_octopi(octopi: dict[Octopus]):
    while True:
        for octopus in octopi:
            octopus.increment()

        flash_count = 0
        for octopus in octopi:
            if octopus.energy > 9:
                flash_count += 1
                octopus.energy = 0

        yield flash_count


def main() -> None:
    # Part One
    octopi = read_octopi()
    assert sum(islice(step_octopi(octopi), 100)) == 1632

    # Part Two
    octopi = read_octopi()
    assert len(list(takewhile(lambda f: f != len(octopi), step_octopi(octopi)))) + 1 == 303


if __name__ == '__main__':
    main()
