import bitstring as bs
from functools import reduce

def read_bitstrings():
	with open('data/day3') as f:
		return list(bs.Bits(bin=line.strip()) for line in f)


def count_ones(bitstrings):
	return reduce(lambda a, b: map(sum, zip(a, b)), bitstrings)


def get_gamma(bitstrings):
	return bs.Bits(map(lambda n: 2 * n >= len(bitstrings), count_ones(bitstrings)))


def life_support(bitstrings, masking_function):
	i = 0
	while len(bitstrings) > 1:
		gamma = masking_function(bitstrings)
		bitstrings = list(filter(lambda bits: bits[i] == gamma[i], bitstrings))
		i += 1

	return bitstrings[0]


def main() -> None:
	# Part One
	gamma = get_gamma(read_bitstrings())
	epsilon = ~gamma
	assert gamma.uint * epsilon.uint == 4191876

	# Part Two
	oxygen = life_support(read_bitstrings(), get_gamma)
	co2 = life_support(read_bitstrings(), lambda x: ~get_gamma(x))

	assert oxygen.uint * co2.uint == 3414905


if __name__ == '__main__':
	main()