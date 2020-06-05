from typing import Any


class Node:
    def __init__(self, value: Any):
        self.value = value
        self.left = None
        self.right = None

    def is_leaf(self) -> bool:
        if self.left is None and self.right is None:
            return True
        return False

    def set_left(self, node: Node) -> None:
        self.left = node

    def set_right(self, node: Node) -> None:
        self.right = node

    def get_left(self) -> Node:
        return self.left

    def get_right(self) -> Node:
        return self.right


class Tree:
    def __init__(self, root: Node):
        self.root = root

    def get_root(self) -> Node:
        return self.root
