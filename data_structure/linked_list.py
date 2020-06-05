class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class DoublyNode(Node):
    def __init__(self, value):
        super().__init__(value)
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_value(self):
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next

    def append(self, new_node: Node):
        current_node = self.head
        while current_node:
            if current_node.next:
                current_node = current_node.next
            else:
                current_node.next = new_node
                break


class DoublyLinkedList(LinkedList):
    def __init__(self):
        super().__init__()

    def append(self, new_node: DoublyNode):
        current_node = self.head

        while current_node:
            if current_node.next:
                current_node = current_node.next
            else:
                current_node.next = new_node
                new_node.prev = current_node
                break
