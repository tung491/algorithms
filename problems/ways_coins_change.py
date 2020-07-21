from typing import List


def ways_coins_chage(n: int, denoms: List[int]):
    ways = [0 for _ in range(n + 1)]
    ways[0] = 1
    for denom in denoms:
        for amount in range(1, n + 1):
            if denom <= amount:
                ways[amount] += ways[amount - denom]
    return ways[n]



def test():
    assert ways_coins_chage(10, [1, 5, 10, 25]) == 4
    assert ways_coins_chage(1, [1, 5, 10, 25]) == 1


if __name__ == '__main__':
    test()  