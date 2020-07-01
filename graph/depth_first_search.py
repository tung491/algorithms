from typing import List


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def add_child(self, name):
        self.children.append(Node(name))

    def depth_first_search(self, array: List[int] = []):
        array.append(self.name)
        for child in self.children:
            child.depth_first_search(array)
        return array
