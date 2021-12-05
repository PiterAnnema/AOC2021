import re


class Board:
	def __init__(self, cells: dict, width: int, height: int) -> None:
		self.cells = cells
		self.col_count = [0] * width
		self.row_count = [0] * height

	@classmethod
	def from_str(cls, s: str):
		n = 3
		cells = dict()
		for i, row in enumerate(s.splitlines()):
			for j, col in enumerate(re.findall(r'\d+', row)):
				cells[int(col)] = (i, j)

		return cls(cells, i + 1, j + 1)

	def mark(self, number: int) -> bool:
		if number in self.cells:
			row, col = self.cells.pop(number)
			self.row_count[row] += 1
			self.col_count[col] += 1

			if self.col_count[col] == len(self.row_count) \
					or self.row_count[row] == len(self.col_count):
				return True

		return False



def read_bingo():
	with open('data/day4') as f:
		blocks = f.read().split('\n\n')

	numbers = list(map(int, blocks[0].split(',')))
	boards = set(map(Board.from_str, blocks[1:]))

	return numbers, boards


def mark_all(number: int, boards: set[Board]) -> set[Board]:
	return set(filter(lambda board: board.mark(number), boards))


def main() -> None:
	# Part One
	numbers, boards = read_bingo()
	for number in numbers:
		winners = mark_all(number, boards)
		if winners:
			winner = winners.pop()
			break

	assert sum(winner.cells) * number == 58838

	# Part Two
	numbers, boards = read_bingo()
	for number in numbers:
		winners = mark_all(number, boards)

		if boards == winners:
			loser = boards.pop()
			break

		boards -= winners

	assert sum(loser.cells) * number == 6256
	

if __name__ == '__main__':
	main()