class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


def branch_sums(root) -> list:
    sums = []
    sums = calculate_branch_sums(root, 0, sums)
    return sums


def calculate_branch_sums(node, running_sum, sums):
    if node is None:
        return sums
    running_sum += node.value
    if node.left is None and node.right is None:
        sums.append(running_sum)
        return sums

    calculate_branch_sums(node.left, running_sum, sums)
    calculate_branch_sums(node.right, running_sum, sums)
