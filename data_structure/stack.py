from linked_list import Node


class Stack:
    def __init__(self):
        self.length = 0
        self.head = None

    def push(self, new_node: Node):
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def pop(self):
        if self.is_empty:
            return None
        temp = self.head.value
        self.head = self.head.next
        self.length -= 1
        return temp

    def top(self):
        if self.head is None:
            return None
        return self.head.value

    @property
    def is_empty(self) -> bool:
        return self.length == 0
