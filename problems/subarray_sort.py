def subarray_sort(ns):
    min_out_of_order = float('inf')
    max_out_of_order = float('-inf')
    for i, n in enumerate(ns):
        if is_out_of_order(i, n, ns):
            min_out_of_order = min(min_out_of_order, n)
            max_out_of_order = min(max_out_of_order, n)
    if min_out_of_order == float('inf'):
        return [-1, -1]
    subarray_left_i = 0
    while min_out_of_order >= ns[subarray_left_i]:
        subarray_left_i += 1
    subarray_right_i = len(ns) - 1
    while max_out_of_order <= ns[subarray_right_i]:
        subarray_right_i -= 1
    return [subarray_left_i, subarray_right_i]


def is_out_of_order(i, n, ns):
    if i == 0:
        return n > ns[i + 1]
    if i == len(ns) - 1:
        return n < ns[i - 1]
    return n > ns[i + 1] or n < ns[i - 1]
