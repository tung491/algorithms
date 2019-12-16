import time
import random
import math


def brute_force_search(a):
    """
    Find the number inversion by using Brute Force Search
    :param a: input list (list)
    :return: inversion_n: the number of inversions of a (int)
    """
    inversion_n = 0
    n = len(a)
    for i in range(n-1):
        for j in range(i+1, n):
            if a[i] > a[j]:
                inversion_n += 1
    return inversion_n


def sort_and_count_inv(a):
    """
    Sort the input list a and count the count the inversion of it
    :param a: input list (list)
    :return: b: sorted list of a (list)
    :return: inversion_n: the number of inversion of a (int)
    """
    n = len(a)
    if n == 0 or n == 1:
        b = a
        inversion_n = 0
    else:
        first_half_a = a[:n//2]
        second_half_a = a[n//2:]
        c, left_inv = sort_and_count_inv(first_half_a)
        d, right_inv = sort_and_count_inv(second_half_a)
        b, split_inv = merge_and_count_split_inv(a, c, d)
        inversion_n = left_inv + right_inv + split_inv
    return b, inversion_n


def merge_and_count_split_inv(a, c, d):
    """
    Merge and count the inversion number which is in both 2 halves
    :param c: input list (list)
    :param: d: input list (list)
    :return split_inv: the number of split inversions (int)
    """
    n = len(c) + len(d)
    b = []
    i, j = 0, 0
    split_inv = 0
    c.append(math.inf)
    d.append(math.inf)
    for k in range(n):
        if c[i] < d[j]:
            b.append(c[i])
            i += 1
        else:
            b.append(d[j])
            j += 1
            split_inv += len(c) - i - 1
    return b, split_inv


def main():
    with open('input_w2.txt') as f:
        data = f.read()
    a = [int(i) for i in data.splitlines()]
    # runtime of Brute Force search
    time_start_1 = time.time()
    inversion_n_1 = brute_force_search(a)
    time_end_1 = time.time()
    # runtime of Divide and Conquer algorithm approach
    time_star_2 = time.time()
    b, inversion_n_2 = sort_and_count_inv(a)
    time_end_2 = time.time()

    print(f'Result of Brute Force Search is {inversion_n_1}. '
          f'Run time is {time_end_1 - time_start_1}')
    print(f'Result of Divide and Conquer algorithm approach '
          f'{inversion_n_2}. Run time is {time_end_2 - time_star_2}')


if __name__ == '__main__':
    main()
