from itertools import pairwise, repeat
from operator import __lt__
from typing import Callable, Iterable


def read_positions() -> list[int]:
    with open('data/day7') as f:
        return list(map(int, f.read().strip().split(',')))


def total_fuel(fuel_fn: Callable[[int, int], int], crabs: Iterable[int], pos: int) -> int:
    return sum(map(fuel_fn, crabs, repeat(pos)))


def last_desc(iterable: Iterable[int]) -> int | None:
    '''Returns the last element for which the iterable was decreasing. 
    Returns none if the iterable is strictly decreasing'''
    for c, d in pairwise(iterable):
        if c < d:
            return c


def main() -> None:
    crabs = read_positions()
    maxpos = max(crabs)
    def fuel_one(crab, pos): return abs(crab - pos)
    assert last_desc((total_fuel(fuel_one, crabs, pos)
                     for pos in range(maxpos))) == 336120

    def intsum(n): return n * (n + 1) // 2
    def fuel_two(crab, pos): return intsum(fuel_one(crab, pos))
    assert last_desc((total_fuel(fuel_two, crabs, pos)
                     for pos in range(maxpos))) == 96864235


if __name__ == '__main__':
    main()
