from itertools import islice, pairwise, starmap, tee
from operator import __lt__


def read_input():
    with open('data/day1') as f:
        yield from map(int, f)


def offset_pairwise(iterable, n):
    '''Return successive pairs, offset by n, taken from the input iterable.
    If n = 1 it is equivalent to itertools.pairwise().'''
    a, b = tee(iterable)
    next(islice(b, n, n), None)
    return zip(a, b)


def one():
    '''Part One'''
    return sum(starmap(__lt__, pairwise(read_input())))


def two():
    '''Part Two'''
    # Since the overlap of the windows does not affect the comparison we can just compare
    # the first and last values of the respective windows.
    # 1 + 2 + 3 < 2 + 3 + 4 is equivalent to 1 < 4
    return sum(starmap(__lt__, offset_pairwise(read_input(), 3)))


def main() -> None:
    print(one())
    print(two())


if __name__ == '__main__':
    main()
