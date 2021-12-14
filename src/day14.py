import re
from collections import defaultdict, Counter
from itertools import pairwise


def read_template():
    steps_pattern = re.compile(r'([A-Z]+) -> ([A-Z]+)')
    with open('data/day14') as f:
        template = next(f).strip()
        steps = {tuple(pair): ins for pair,
                 ins in steps_pattern.findall(f.read())}

    return template, steps


def apply_steps(pairs: dict, steps: dict, freq: dict):
    new_pairs = defaultdict(int)
    for pair, count in pairs.items():
        c = steps[pair]
        freq[c] += count
        new_pairs[pair[0], c] += count
        new_pairs[c, pair[1]] += count

    return new_pairs



def main() -> None:
    template, steps = read_template()

    freq = Counter(template)
    pairs = Counter(pairwise(template))

    # Part One
    for _ in range(10):
        pairs = apply_steps(pairs, steps, freq)
    assert max(freq.values()) - min(freq.values()) == 2194

    # Part ~Two
    for _ in range(30):
        pairs = apply_steps(pairs, steps, freq)
    assert max(freq.values()) - min(freq.values()) == 2360298895777



if __name__ == '__main__':
    main()
