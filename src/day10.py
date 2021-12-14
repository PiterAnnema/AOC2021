from __future__ import annotations
from dataclasses import dataclass
from functools import reduce
from itertools import filterfalse, repeat


def read_commands():
    with open('data/day10') as f:
        yield from map(str.strip, f)


@dataclass
class Chunk:
    delimiter: str
    prevval: Chunk


class CommandParser:
    pairs = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }

    def __init__(self, command: str) -> None:
        self.command = command
        self.head = None

    def errors(self):
        self.head = None
        for c in self.command:
            if c in self.pairs:
                # Opening character
                chunk = Chunk(self.pairs[c], self.head)
                self.head = chunk

            else:
                if self.head is None or self.head.delimiter != c:
                    # Illegal character
                    yield c
                else:
                    # Closing character
                    self.head = self.head.prevval

    def parse(self):
        return list(self.errors())

    def complete(self):
        while self.head:
            yield self.head.delimiter
            self.head = self.head.prevval


def score_two(parser: CommandParser, values: dict):
    return reduce(lambda a, b: a * 5 + b, map(values.get, parser.complete()))


def one():
    '''Part One'''
    values_one = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }

    parsers = map(CommandParser, read_commands())
    errors = map(CommandParser.errors, parsers)
    first_errors = filter(None, map(next, errors, repeat(None)))
    return sum(map(values_one.get, first_errors))


def two():
    '''Part Two'''
    values_two = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4,
    }
    parsers = map(CommandParser, read_commands())
    no_errors = filterfalse(lambda p: any(p.errors()), parsers)
    scores = sorted(map(score_two, no_errors, repeat(values_two)))
    return scores[len(scores) // 2]


def main() -> None:
    print(one())
    print(two())


if __name__ == '__main__':
    main()
