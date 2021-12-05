import re
from dataclasses import dataclass
from itertools import filterfalse, chain
from typing import NamedTuple
from collections import Counter
from operator import __add__


def sign(n: int) -> int:
	if n < 0:
		return -1

	if n > 0:
		return 1

	return 0
	

class Point(NamedTuple):
	x: int
	y: int

	def __add__(self, other: object) -> object:
		return self.__class__(*map(__add__, self, other))



@dataclass
class Segment:
	start: Point
	end: Point
	_unit: Point = None

	def covers(self) -> set[Point]:
		point = self.start
		while point != self.end:
			yield point
			point = point + self.unit

		yield point

	@property
	def unit(self):
		if self._unit is None:
			dx = self.end.x - self.start.x
			dy = self.end.y - self.start.y

			self._unit = Point(sign(dx), sign(dy))

		return self._unit

	def is_diagonal(self):
		return all(self.unit)


def read_segments():
	pattern = re.compile(r'(?:(\d+),(\d+))')
	with open('data/day5') as f:
		for line in f:
			start, end = pattern.findall(line) 
			yield Segment(Point(*map(int, start)), Point(*map(int, end)))



def main() -> None:
	# Part One
	segments = filterfalse(Segment.is_diagonal, read_segments())
	covered = Counter(chain(*map(Segment.covers, segments)))
	assert sum(map(lambda n: n > 1, covered.values())) == 4993

	# Part Two
	segments = read_segments()
	covered = Counter(chain(*map(Segment.covers, segments)))
	assert sum(map(lambda n: n > 1, covered.values())) == 21101


if __name__ == '__main__':
	main()