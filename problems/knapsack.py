def solve():
    inputs = [
        [1, 2],
        [4, 3],
        [5, 6],
        [6, 7]
    ]
    limit = 10
    weights = [0 for _ in range(limit+1)]
    for v, w in inputs:
        for i, weight in enumerate(weights):
            if w + weight > limit:
                continue
            curr_value = v + i
            if weights[weight + w] < curr_value:
                weights[weight + w] = curr_value
    print(weights[limit])


if __name__ == '__main__':
    solve()