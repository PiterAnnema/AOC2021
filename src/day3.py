from functools import reduce
from operator import __add__

import bitstring as bs


def read_bitstrings():
    with open('data/day3') as f:
        return list(bs.Bits(bin=line.strip()) for line in f)


def count_ones(bitstrings):
    return reduce(lambda a, b: map(__add__, a, b), bitstrings)


def get_gamma(bitstrings):
    return bs.Bits(map(lambda n: 2 * n >= len(bitstrings), count_ones(bitstrings)))


def life_support(bitstrings, masking_function):
    i = 0
    while len(bitstrings) > 1:
        gamma = masking_function(bitstrings)
        bitstrings = list(filter(lambda bits: bits[i] == gamma[i], bitstrings))
        i += 1

    return bitstrings[0]


def one():
    '''Part One'''
    gamma = get_gamma(read_bitstrings())
    epsilon = ~gamma
    return gamma.uint * epsilon.uint


def two():
    '''Part Two'''
    oxygen = life_support(read_bitstrings(), get_gamma)
    co2 = life_support(read_bitstrings(), lambda x: ~get_gamma(x))

    return oxygen.uint * co2.uint


def main() -> None:
    print(one())
    print(two())


if __name__ == '__main__':
    main()
