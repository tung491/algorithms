import math
import random
import sys
import time

sys.setrecursionlimit(5000)


def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    dist = math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))
    return dist


def brute_force_search(px):
    min_dist = distance(px[0], px[1])
    n = len(px)
    p1, p2 = px[0], px[1]
    closest_pair = ()
    if n == 2:
        closest_pair = (p1, p2)
    for i in range(n - 1):
        for j in range(i + 1, n):
            p1, p2 = px[i], px[j]
            ps_dist = distance(p1, p2)
            if ps_dist < min_dist:
                min_dist = ps_dist
                closest_pair = (p1, p2)
    return closest_pair


def find_closest_pair(px, py):
    n = len(px)
    if n <= 3:
        return brute_force_search(px)
    half_n = n // 2
    left_px = px[:half_n]
    right_px = px[half_n:]
    left_py = py[:half_n]
    right_py = py[half_n:]

    l1, l2 = find_closest_pair(left_px, left_py)
    r1, r2 = find_closest_pair(right_px, right_py)
    pairs = [(l1, l2), (r1, r2)]
    best_pair, min_dist = min([(pair, distance(*pair)) for pair in pairs],
                              key=lambda x:x[1])
    s1, s2 = closest_split_pair(px, py, min_dist, best_pair)
    pairs.append((s1, s2))
    pairs = [(pair, distance(*pair)) for pair in pairs]
    closest_pair = min(pairs, key=lambda x: x[1])[0]
    return closest_pair


def closest_split_pair(px, py, delta, best_pair):
    half_n = len(px) // 2
    left_px = px[:half_n]
    x_median = left_px[-1][0]
    s_y = []
    for point in py:
        if x_median - delta <= point[0] <= x_median + delta:
            s_y.append(point)

    best = delta
    len_sy = len(s_y)
    for i in range(len_sy - 1):
        for j in range(i + 1, min(7, len_sy)):
            dist = distance(s_y[i], s_y[j])
            if dist < best:
                best = dist
                best_pair = (s_y[i], s_y[j])
    return best_pair


def main():
    x = [random.randint(1, 200) for _ in range(16)]
    y = [random.randint(1, 200) for _ in range(16)]
    p = list(zip(x, y))
    px = sorted(p, key=lambda x: x[0])
    py = sorted(p, key=lambda x: x[1])
    # Brute Search
    start = time.time()
    closest_pair_1 = brute_force_search(px)
    end = time.time()
    print(f'Brute Force Search:\n '
          f'Closest pair is {closest_pair_1}\n'
          f'Run time is {end - start}')
    # Divide and Conquer algorithm
    start = time.time()
    closest_pair_2 = find_closest_pair(px, py)
    end = time.time()
    print(f'Divide and Conquer Algorithm:\n '
          f'Closest pair is {closest_pair_2}\n'
          f'Run time is {end - start}')


if __name__ == '__main__':
    main()
