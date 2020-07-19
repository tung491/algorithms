from typing import List


def has_single_cycle(ns: List[int]):
    visited_n = 0
    curr_i = 0
    while visited_n < len(ns):
        if visited_n > 0 and curr_i == 0:
            return False
        visited_n += 1
        curr_i = get_next_i(curr_i, ns)
    return curr_i == 0


def get_next_i(curr_i: int, ns: List[int]):
    jump = ns[curr_i]
    next_i = (curr_i + jump) % len(ns)
    return next_i if next_i >= 0 else next_i + len(ns)


def test():
    ns = [2, 3, 1, -4, -4, 2]
    assert has_single_cycle(ns)


if __name__ == '__main__':
    test()
