def read_entries():
    with open('data/day8') as f:
        for line in f:
            entry_in, entry_out = line.strip().split(' | ')
            yield entry_in.split(' '), entry_out.split(' ')


def get_candidates(digit, overlap, segments, solution):
    for i, s in enumerate(segments):
        if len(digit) == len(s) and all(overlap[i][j] == len(digit & sol) for sol, j in solution.items()):
            yield i


def solve_entry(entry_in, entry_out, overlap, segments):
    entry = set(map(frozenset, entry_in + entry_out))

    solution = dict()
    while len(solution) < len(segments):
        for digit in entry.difference(solution):
            candidates = list(get_candidates(
                digit, overlap, segments, solution))
            if len(candidates) == 1:
                solution[digit] = candidates.pop()

    return solution


def main() -> None:
    # Part One
    assert sum(sum(len(digit) in [2, 3, 4, 7] for digit in entry_out)
               for _, entry_out in read_entries()) == 383

    # Part Two
    segments = list(map(set, ['abcefg', 'cf', 'acdeg', 'acdfg',
                    'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']))

    # Make a lookup-table of the overlap between digits. This produces a unique signature for each digit.
    overlap = [[len(a & b) for a in segments] for b in segments]

    sm = 0
    for entry_in, entry_out in read_entries():
        solution = solve_entry(entry_in, entry_out, overlap, segments)

        sm += int(''.join(str(solution[frozenset(d)]) for d in entry_out))

    assert sm == 998900


if __name__ == '__main__':
    main()
