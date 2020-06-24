from typing import List


# Approach for unsorted input list
def unsorted_two_number_sum(input_list: List[int], target: int) -> List[int]:
    """
    Return a list of 2 two numbers which sum of them equals target
    :param input_list:
    :param target:
    """
    for i, first_n in enumerate(input_list):
        for j, second_n in enumerate(input_list[i + 1:], start=i + 1):
            if first_n + second_n == target:
                return [first_n, second_n]
    return []


# Approach for sorted input list
def sorted_two_number_sum(input_list: List[int], target: int) -> List[int]:
    """
    Return a list of 2 two numbers which sum of them equals target
    :param input_list:
    :param target:
    """
    left_i = 0
    right_i = len(input_list) - 1
    while left_i < right_i:
        curr_sum = input_list[left_i] + input_list[right_i]
        if curr_sum == target:
            return [input_list[left_i], input_list[right_i]]
        elif curr_sum < target:
            left_i += 1
        else:
            right_i -= 1
    return []


if __name__ == '__main__':
    print(unsorted_two_number_sum([1, 5, 3, 4, 2], 3))
    print(sorted_two_number_sum([1, 2, 6, 7, 8, 9], 10))
