def validate_bst(tree):
    return validate_bst_helper(tree, float('inf'), float('inf'))


def validate_bst_helper(tree, min_value, max_value):
    if tree is None:
        return True
    if tree.value not in range(min_value, max_value):
        return False
    
    left_is_vaild = validate_bst_helper(tree.left, min_value, tree.value)
    right_is_vaild = validate_bst_helper(tree.right, tree.value, max_value)
    return left_is_vaild and right_is_vaild
