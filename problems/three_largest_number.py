import math
from typing import List


def find_three_largest_nums(input_list: List[int]) -> List[int]:
    largests = [-math.inf] * 3
    for num in input_list:
        if num > largests[0]:
            largests = [num] + largests[:2]
        elif num > largests[1]:
            largests[1], largests[2] = num, largests[1]
        elif num > largests[2]:
            largests[2] = num
    return largests


if __name__ == '__main__':
    print(find_three_largest_nums([141, 1, 16, 12, 14, 4, 5]))
