import heapq
from typing import Callable, TypeVar


def read_cavern() -> dict[tuple, int]:
    with open('data/day15') as f:
        cavern = {(i, j): int(r) for i, line in enumerate(f)
                  for j, r in enumerate(line.strip())}

    return cavern


def get_neighbors(u: tuple):
    i, j = u
    return {(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)}


T = TypeVar('T')


def a_star(start: T, target: T, d: Callable, h: Callable, n: Callable) -> dict[T]:
    '''Pretty straightforward A* algorithm with a priority queue.'''
    queue = []
    heapq.heappush(queue, (0, start))

    # We won't resolve the path for this question
    # prev = dict()

    g_scores = dict()
    g_scores[start] = 0

    f_scores = dict()
    f_scores[start] = 0

    while queue and (u := heapq.heappop(queue)[1]) != target:
        for v in n(u):
            new_gscore = g_scores[u] + d(u, v)
            if v not in g_scores or new_gscore < g_scores[v]:
                # prev[v] = u
                g_scores[v] = new_gscore
                f_scores[v] = new_gscore + h(v)

                heapq.heappush(queue, (f_scores[v], v))

    return g_scores


def one():
    '''Part One'''
    cavern = read_cavern()
    start = (0, 0)
    target = max(cavern)

    def d(_, v):
        return cavern[v]

    def h(v):
        return target[0] - v[0] + target[1] - v[1]

    def n(u):
        return filter(lambda v: 0 <= v[0] <= target[0] and 0 <= v[1] <= target[1], get_neighbors(u))

    dist = a_star(start, target, d, h, n)
    return dist[target]


def two():
    '''Part Two'''
    cavern = read_cavern()
    mi, mj = max(cavern)
    width = mi + 1
    height = mj + 1

    start = (0, 0)
    target = (5 * height - 1, 5 * width - 1)

    def d(_, v):
        i, j = v
        return (cavern[i % height, j % width] + i // height + j // width - 1) % 9 + 1

    def h(v):
        return target[0] - v[0] + target[1] - v[1]

    def n(u):
        return filter(lambda v: 0 <= v[0] <= target[0] and 0 <= v[1] <= target[1], get_neighbors(u))

    dist = a_star(start, target, d, h, n)
    return dist[target]


def main() -> None:
    print(one())
    print(two())


if __name__ == '__main__':
    main()
