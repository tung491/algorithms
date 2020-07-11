import deque


def bfs(root):
    queue = deque.deque()
    queue.put(root)
    order = []

    while queue:
        node = queue.popleft()
        for child in node.children:
            if child is not None:
                queue.put(child)
        order.append(node)
    return order