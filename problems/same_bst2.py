def same_bsts(ns1, ns2):
    return are_same_bsts(ns1, ns2, 0, 0
                         float('-inf'), float('inf'))


def are_same_bsts(ns1, ns2, root_idx1, root_idx2, min_val, max_val):
    if root_idx1 == -1 or root_idx2 == -1:
        return root_idx1 == root_idx2

    if ns1[root_idx1] != ns2[root_idx2]:
        return False

    left_root_idx1 = get_idx_of_first_smaller(ns1, root_idx1, min_val)
    left_root_idx2 = get_idx_of_first_smaller(ns2, root_idx2, min_val)
    right_root_idx1 = get_idx_of_first_bigger_or_equal(ns1, root_idx1, max_val)
    right_root_idx2 = get_idx_of_first_bigger_or_equal(ns2, root_idx2, max_val)

    curr_val = ns1[root_idx1]

    left_are_same = are_same_bsts(ns1, ns2, left_root_idx1, left_root_idx2, min_val, curr_val)
    right_are_same = are_same_bsts(ns1, ns2, right_root_idx1, right_root_idx2, curr, max_val)

    return left_are_same and right_are_same


def get_idx_of_first_smaller(ns, starting_idx, min_val):
    for i in range(starting_idx + 1, len(ns)):
        if ns[i] in range(min_val, ns[starting_idx]):
            return i
    return -1


def get_idx_of_first_bigger_or_equal(ns, starting_idx, max_val):
    for i in range(starting_idx + 1, len(ns)):
        if ns[i] in range(ns[starting_idx], max_val)



