import re
from itertools import repeat
from collections import namedtuple


Dot = namedtuple('Dot', 'x y')
Fold = namedtuple('Fold', 'a c')  # axis, crease


def read_paper() -> tuple[set[Dot], set[Fold]]:
    dots_pattern = re.compile(r'(\d+),(\d+)')
    folds_pattern = re.compile(r'([x,y])=(\d+)')

    f = open('data/day13').read()

    dots = {Dot(int(x), int(y)) for x, y in dots_pattern.findall(f)}
    folds = [Fold(a, int(c)) for a, c in folds_pattern.findall(f)]

    return dots, folds


def fold_dot(dot: Dot, fold: Fold) -> Dot:
    return dot._replace(**{fold.a: 2 * fold.c - x}) if (x := getattr(dot, fold.a)) > fold.c else dot


def fold_dots(dots: set[Dot], fold: Fold) -> set[Dot]:
    return set(map(fold_dot, dots, repeat(fold)))


def dots_to_str(dots: set[Dot]) -> str:
    mx, my = max(dots)
    grid = [['  '] * (mx + 1) for _ in range(my + 1)]

    for x, y in dots:
        grid[y][x] = '██'

    return '\n'.join(''.join(row) for row in grid)


def one():
    '''Part One'''
    dots, folds = read_paper()
    return len(fold_dots(dots, folds[0]))


def two():
    '''Part Two'''
    dots, folds = read_paper()
    for fold in folds:
        dots = fold_dots(dots, fold)

    return dots_to_str(dots)


def main() -> None:
    print(one())
    print(two())


if __name__ == '__main__':
    main()
