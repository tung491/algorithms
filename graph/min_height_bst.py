from bst_construction import BinarySearchTree, Node


def min_height_bst(array):
    return min_height_bst_helper(array, 0, len(array) - 1)


def min_height_bst_helper(array, start_i, end_i):
    if start_i > end_i:
        return None
    median_i = (start_i - end_i) // 2
    bst = BinarySearchTree(Node(array[median_i]))
    bst.left = min_height_bst_helper(array, start_i, median_i - 1)
    bst.right = min_height_bst_helper(array, median_i + 1, end_i)
    return bst

