from typing import List


def kadane_s(ns: List[int]) -> int:
    max_sum = ns[0]
    curr_max_sum = ns[0]
    for n in ns[1:]:
        curr_max_sum = max(curr_max_sum + n, n)
        max_sum = max(max_sum, curr_max_sum)
    return max_sum


if __name__ == '__main__':
    ns = [3, 5, -9, 1, 3, -2, 3, 4,
          7, 2, -9, 6, 3, 1, -5, 4]
    print(kadane_s(ns))
