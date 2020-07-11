def inorder_traversal(tree, order):
    if tree is not None:
        inorder_traversal(tree.left, order)
        order.append(tree.value)
        inorder_traversal(tree.right, order)
    return order


def preorder_traversal(tree, order):
    if tree is not None:
        order.append(tree.value)
        preorder_traversal(tree.left, order)
        preorder_traversal(tree.right, order)
    return order
    

def postorder_traversal(tree, order):
    if tree is not None:
        postorder_traversal(tree.left, order)
        postorder_traversal(tree.right, order)
        order.append(tree.value)
    return order
