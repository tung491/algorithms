import math


def min_coins_for_change(amount, denoms):
    coin_nums = [math.inf for _ in range(amount + 1)]
    coin_nums[0] = 0
    for denom in denoms:
        for curr_amount in range(amount + 1):
            if denom <= curr_amount:
                remain = curr_amount - denom
                coin_nums[curr_amount] = min(coin_nums[remain] + 1, coin_nums[curr_amount])
    return coin_nums[-1] if coin_nums[-1] != math.inf else -1


def test():
    print(min_coins_for_change(6, [1, 2, 4]))


if __name__ == "__main__":
    test()
