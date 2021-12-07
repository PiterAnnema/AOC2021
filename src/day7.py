from typing import Generator, Iterable, Callable
from functools import partial
from operator import __lt__
from itertools import pairwise


def read_positions() -> list[int]:
	with open('data/day7') as f:
		return list(map(int, f.read().strip().split(',')))


def total_fuel(fuel_fn: Callable[[int, int], int], crabs: Iterable[int], pos: int) -> int:
	return sum(map(partial(fuel_fn, pos=pos), crabs))


def last_desc(iterable: Iterable[int]) -> int|None:
	'''Returns the last element for which the iterable was decreasing. 
	Returns none if the iterable is strictly decreasing'''
	for c, d in pairwise(iterable):
		if c < d:
			return c


def main() -> None:
	crabs = read_positions()
	maxpos = max(crabs)
	fuel_one = lambda crab, pos: abs(crab - pos)
	assert last_desc((total_fuel(fuel_one, crabs, pos) for pos in range(maxpos))) == 336121

	intsum = lambda n: n * (n + 1) // 2
	fuel_two = lambda crab,    pos: intsum(fuel_one(crab, pos))
	assert last_desc((total_fuel(fuel_two, crabs, pos) for pos in range(maxpos))) == 96864235


if __name__ == '__main__':
	main()