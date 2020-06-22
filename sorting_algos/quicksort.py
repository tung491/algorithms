import random


def quick_sort(input_list: list) -> list:
    quick_sort_helper(input_list, 0, len(input_list) - 1)
    return input_list


def quick_sort_helper(array, start_i, end_i):
    def swap(i, j):
        array[i], array[j] = array[j], array[i]

    if start_i >= end_i:
        return
    pivot_i = start_i
    left_i = start_i + 1
    right_i = end_i

    while right_i >= left_i:
        if array[left_i] > array[pivot_i] > array[right_i]:
            swap(left_i, right_i)
        if array[left_i] <= array[pivot_i]:
            left_i += 1
        if array[right_i] >= array[pivot_i]:
            right_i -= 1
    swap(pivot_i, right_i)
    left_subarray_smaller = right_i - 1 - start_i < end_i - (right_i + 1)
    if left_subarray_smaller:
        quick_sort_helper(array, start_i, right_i - 1)
        quick_sort_helper(array, right_i + 1, end_i)
    else:
        quick_sort_helper(array, right_i + 1, end_i)
        quick_sort_helper(array, start_i, right_i - 1)


if __name__ == '__main__':
    print(quick_sort([1, 4, 6, 2, 3]))

