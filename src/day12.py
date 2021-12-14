from collections import defaultdict


def read_caves():
    '''Construct a directed graph of caves. 
    The end cave doesn't anywhere.
    No caves go to start.'''
    caves = defaultdict(set)
    with open('data/day12') as f:
        for line in f:
            a, b = line.strip().split('-')
            if b != 'start':
                caves[a].add(b)
            if a != 'start' and b != 'end':
                caves[b].add(a)

    return caves


def find_paths(caves: dict[set], curr: str, double_visit: bool, path: list[str]):
    if curr.islower() and curr in path:
        if not double_visit:
            return

        double_visit = False

    path = path + [curr]

    if curr == 'end':
        yield path
        return

    for cave in caves[curr]:
        yield from find_paths(caves, cave, double_visit, path)


def one():
    '''Part One'''
    return len(list(find_paths(read_caves(), 'start', False, [])))


def two():
    '''Part Two'''
    return len(list(find_paths(read_caves(), 'start', True, [])))


def main() -> None:
    print(one())
    print(two())


if __name__ == '__main__':
    main()
