from itertools import pairwise, starmap
from operator import __lt__


def main() -> None:
	with open('data/day1') as f:
		print(sum(starmap(__lt__, pairwise(map(int, f)))))


if __name__ == '__main__':
	main()