def depth_first_search(root, order):
    order.append(root)
    for child in root.children:
        depth_first_search(child, order)
    return order
