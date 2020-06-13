def swap(i: int, j: int, input_list: list) -> list:
    input_list[i], input_list[j] = input_list[j], input_list[i]
    return input_list


def bubble_sort(input_list: list) -> list:
    is_sorted = False
    end_index = len(input_list) - 1
    while not is_sorted:
        is_sorted = True
        for i in range(end_index):
            if input_list[i] > input_list[i + 1]:
                swap(i, i + 1, input_list)
                is_sorted = False
        end_index -= 1
    return input_list


if __name__ == '__main__':
    print(bubble_sort([1, 3, 5, 8, 11, 2]))

