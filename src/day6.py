from itertools import islice
from typing import Counter


def read_fish():
    fish = [0] * 9
    with open('data/day6') as f:
        # No need to keep track of all fish, just group them by day
        for i in map(int, f.read().strip().split(',')):
            fish[i] += 1

    return fish


def simulate_fish(fish: list):
    day = 0
    while True:
        i = day % 7
        t = fish[7]
        fish[7] = fish[8]
        fish[8] = fish[i]
        fish[i] += t
        day += 1

        yield fish


def consume(iterator, n):
    '''Advance the iterator by n steps'''
    next(islice(iterator, n, n), None)


def one():
    '''Part One'''
    sim = simulate_fish(read_fish())
    consume(sim, 80 - 1)
    return sum(next(sim))


def two():
    '''Part Two'''
    sim = simulate_fish(read_fish())
    consume(sim, 256 - 1)
    return sum(next(sim))


def main() -> None:
    print(one())
    print(two())


if __name__ == '__main__':
    main()
