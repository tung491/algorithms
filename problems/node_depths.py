def node_depths(root, depth = 0):
    if root is None:
        return 0
    return depth + node_depths(root.left, depth + 1) + node_depths(root.right, depth + 1)
