from typing import List


def max_sum_inc_subsequence(ns: List[int]):
    prevs = [None] * len(ns)
    sums = ns[:]
    max_idx = 0
    for i, curr_n in enumerate(ns):
        for j, other_n in enumerate(ns[:i]):
            if other_n < curr_n and sums[j] + curr_n >= sums[i]:
                sums[i] = sums[j] + curr_n
                prevs[i] = j
        if sums[i] >= sums[max_idx]:
            max_idx = i
    return [sums[max_idx], gen_sequence(prevs, ns, max_idx)]


def gen_sequence(prevs, ns, curr_idx):
    sequence = []
    while curr_idx is not None:
        sequence.insert(0, ns[curr_idx])
        curr_idx = prevs[curr_idx]
    return sequence


if __name__ == '__main__':
    print(max_sum_inc_subsequence([8, 12, 2, 3, 15, 5, 7]))