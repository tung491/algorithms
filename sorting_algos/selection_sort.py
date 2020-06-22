def selection_sort(input_list: list) -> list:
    """
    Selection sort algorithm
    Space Complexity: O(1)
    Time Complexity: O(n^2)
    :param input_list:
    :return:
    """
    def swap(i, j):
        input_list[i], input_list[j] = input_list[j], input_list[i]

    curr_i = 0
    min_i = 0
    while curr_i < len(input_list) - 1:
        min_n = input_list[curr_i]

        for j, n in enumerate(input_list[curr_i+1:], start=curr_i+1):
            if n < min_n:
                min_n = n
                min_i = j
        swap(curr_i, min_i)
        curr_i += 1
    return input_list


if __name__ == '__main__':
    print(selection_sort([1, 3, 2, 3, 2, 12, 3, 4]))