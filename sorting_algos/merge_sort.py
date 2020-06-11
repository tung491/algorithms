def merge_sort(input_list: list) -> list:
    if len(input_list) <= 1:
        return input_list

    middle = len(input_list) // 2
    left = input_list[:middle]
    right = input_list[middle:]
    left = merge_sort(left)
    right = merge_sort(right)

    merged_list = merge(left, right)
    return merged_list


def merge(left: list, right: list) -> list:
    merge_list = []
    i, j = 0, 0

    while i < len(left) or j < len(right):
        if i == len(left):
            merge_list.append(right[j])
            j += 1
            continue
        elif j == len(right):
            merge_list.append(left[i])
            i += 1
            continue
        if left[i] < right[j]:
            merge_list.append(left[i])
            i += 1
        else:
            merge_list.append(right[j])
            j += 1
    return merge_list
