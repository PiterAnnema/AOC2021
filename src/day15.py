import heapq
from typing import Callable, TypeVar


def read_cavern() -> dict[tuple, int]:
    with open('data/day15') as f:
        cavern = {(i, j): int(r) for i, line in enumerate(f)
                  for j, r in enumerate(line.strip())}

    return cavern


def get_neighbors(i: int, j: int):
    return ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1))


T = TypeVar('T')


def dijkstra(start: T, target: T, d: Callable, n: Callable) -> dict[T]:
    '''Pretty straightforward Dijkstra algorithm with a priority queue.'''
    queue = [(0, start)]

    # We won't resolve the path for this question
    # prev = dict()

    dist = {start: 0}

    while queue and (u := heapq.heappop(queue)[1]) != target:
        for v in n(u):
            if v in dist:
                continue
            score = dist[u] + d(u, v)
            if v not in dist or score < dist[v]:
                # prev[v] = u
                dist[v] = score

                heapq.heappush(queue, (score, v))

    return dist


def one():
    '''Part One'''
    cavern = read_cavern()
    start = (0, 0)
    target = max(cavern)

    def d(_, v):
        return cavern[v]

    def n(u):
        return filter(lambda v: 0 <= v[0] <= target[0] and 0 <= v[1] <= target[1], get_neighbors(*u))

    dist = dijkstra(start, target, d, n)
    return dist[target]


def two():
    '''Part Two'''
    cavern = read_cavern()
    mi, mj = max(cavern)
    width, height = mi + 1, mj + 1

    start = (0, 0)
    target = (5 * height - 1, 5 * width - 1)

    def d(_, v):
        i, j = v
        return (cavern[i % height, j % width] + i // height + j // width - 1) % 9 + 1

    def n(u):
        i, j = u
        return filter(lambda v: 0 <= i <= target[0] and 0 <= j <= target[1], get_neighbors(i, j))

    dist = dijkstra(start, target, d, n)
    return dist[target]


def main() -> None:
    print(one())
    print(two())


if __name__ == '__main__':
    main()
