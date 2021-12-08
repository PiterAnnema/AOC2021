from itertools import islice


def read_fish():
    with open('data/day6') as f:
        return map(int, f.read().strip().split(','))


def simulate_fish(fish: list):
    day = 0
    while True:
        i = day % 7
        t = fish[7]
        fish[7] = fish[8]
        fish[8] = fish[i]
        fish[i] += t
        day += 1

        yield fish


def consume(iterator, n):
    '''Advance the iterator by n steps'''
    next(islice(iterator, n, n), None)


def main() -> None:
    # No need to keep track of all fish, just group them by day
    fish = [0] * 9
    for f in read_fish():
        fish[f] += 1

    sim = simulate_fish(fish)

    # Part One
    day1 = 80
    consume(sim, day1 - 1)
    assert sum(next(sim)) == 380758

    # Part Two
    day2 = 256
    consume(sim, day2 - day1 - 1)
    assert sum(next(sim)) == 1710623015163


if __name__ == '__main__':
    main()
