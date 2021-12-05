from dataclasses import dataclass

@dataclass
class Position:
	x: int = 0
	y: int = 0

	@property
	def depth(self):
		return - self.y

	def forward(self, value):
		self.x += value

	def up(self, value):
		self.y += value

	def down(self, value):
		self.up(- value)


@dataclass
class AimedPosition(Position):
	aim: int = 0

	def forward(self, value):
		super().forward(value)
		super().up(value * self.aim)

	def up(self, value):
		self.aim += value


def read_commands():
	with open('data/day2') as f:
		for line in f:
			command, value = line.split()
			yield command, int(value)


def execute_commands(commands, pos):
	for command, value in commands:
		getattr(pos, command)(value)


def main() -> None:
	# Part One
	pos = Position()
	execute_commands(read_commands(), pos)
	assert pos.x * pos.depth == 1714680

	# Part Two
	pos = AimedPosition()
	execute_commands(read_commands(), pos)
	assert pos.x * pos.depth == 1963088820


if __name__ == '__main__':
	main()