from typing import List


def product_sum(input_list: List[int], multiplier: int = 1) -> int:
    """
    Calculate the result by multiply the sum of list with multiplier
    Space Complexity: O(D)
    Time Complexity: O(n)
    :param input_list:
    :param multiplier:
    :return: int
    """
    sum_ = 0
    for n in input_list:
        if isinstance(n, list):
            sum_ += product_sum(n, multiplier + 1)
        else:
            sum_ += n
    return sum_ * multiplier


if __name__ == '__main__':
    print(product_sum([1, 2, 3]))
