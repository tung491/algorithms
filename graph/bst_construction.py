class BinarySearchTree:
    def __init__(self, root_value):
        self.value = root_value
        self.left = None
        self.right = None
        self.children = [self.left, self.right]

    def insert(self, value):
        curr_node = self
        while True:
            if value < curr_node.value:
                if curr_node.left is not None:
                    curr_node.left = BinarySearchTree(value)
                    break
                else:
                    curr_node = curr_node.left
            else:
                if curr_node.right is not None:
                    curr_node.right = BinarySearchTree(value)
                    break
                else:
                    curr_node = curr_node.right
        return self

    def contains(self, value):
        curr_node = self
        while curr_node is not None:
            if value < curr_node.value:
                curr_node = curr_node.left
            elif value > curr_node.value:
                curr_node = curr_node.right
            else:
                return True
        return False

    def remove(self, value, parent_node=None):
        curr_node = self
        while curr_node is not None:
            if value < curr_node.value:
                parent_node = curr_node
                curr_node = curr_node.left
            elif value > curr_node.value:
                parent_node = curr_node
                curr_node = curr_node.right
            else:
                if all(child is not None for child in self.children):
                    min_right_value = curr_node.right.get_min_value()
                    curr_node.value = min_right_value
                    curr_node.right.remove(min_right_value, curr_node)
                elif parent_node is not None:
                    if curr_node.left:
                        curr_node.value = curr_node.left.value
                        curr_node.right = curr_node.left.right
                        curr_node.left = curr_node.left.left
                    elif curr_node.right is not None:
                        curr_node.value = curr_node.right.value
                        curr_node.left = curr_node.right.left
                        curr_node.right = curr_node.right.right
                    else:
                        curr_node.value = None
                elif parent_node.left == curr_node:
                    parent_node.left = curr_node.left if curr_node.left else curr_node.right
                elif parent_node.right == curr_node:
                    parent_node.right = curr_node.left if curr_node.left else curr_node.right
                break
        return self

    def get_min_value(self):
        curr_node = self
        while curr_node.left is not None:
            curr_node = curr_node.left
        return curr_node.valu is not None
