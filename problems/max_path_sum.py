def max_path_sum(tree):
    return find_max_sum(tree)[1]


def find_max_sum(tree):
    if tree is None:
        return 0, 0

    left_max_branch_sum, left_max_path_sum = find_max_sum(tree.left)
    right_max_branch_sum, right_max_path_sum = find_max_sum(tree.right)
    max_child_sum_as_branch = max(left_max_branch_sum, right_max_branch_sum)
    value = tree.value
    max_branch_sum = max(max_child_sum_as_branch + value, value)
    max_sum_root_node = max(left_max_branch_sum + value + right_max_branch_sum, max_branch_sum)
    max_path_sum = max(left_max_path_sum, right_max_path_sum, max_sum_root_node)
    return max_branch_sum, max_path_sum
