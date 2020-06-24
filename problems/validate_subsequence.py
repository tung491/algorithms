from typing import List


def validate_subsequence(input_list: List[int], sequence: List[int]) -> bool:
    """
    Validate that Do input_list contains all elements in sequence
    Space Complexity: O(1)
    Time Complexity: O(1)

    :param input_list:
    :param sequence:
    :return: bool
    """
    seq_i = 0
    for n in input_list:
        if seq_i == len(sequence):
            break
        if sequence[seq_i] == n:
            seq_i += 1
    return seq_i == len(sequence)


if __name__ == '__main__':
    print(validate_subsequence(list(range(10)), [2, 4, 5, 6]))