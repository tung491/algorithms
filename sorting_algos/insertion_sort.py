def swap(i: int, j: int, input_list: list) -> list:
    input_list[i], input_list[j] = input_list[j], input_list[i]
    return input_list


def insertion_sort(input_list: list) -> list:
    for i in range(1, len(input_list)):
        j = i
        while j > 0 and input_list[j] < input_list[j - 1]:
            swap(j, j - 1, input_list)
            j -= 1
    return input_list


if __name__ == '__main__':
    print(insertion_sort([1, 3, 2, 5, 6, 10, 2]))