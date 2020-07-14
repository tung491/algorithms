def invert_bst(root):
    if root is None:
        return root
    root.left, root.right = root.right, root.left
    invert_bst(root.left)
    invert_bst(root.right)