from typing import *


class Node(object):
    left: Optional['Node']
    right: Optional['Node']

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        if self.root is None:
            self.root = Node(new_val)
            return

        current_node = self.root

        while True:
            if current_node.value > new_val:
                if current_node.left is None:
                    current_node.left = Node(new_val)
                    return
                else:
                    current_node = current_node.left

            else:
                if current_node.right is None:
                    current_node.right = Node(new_val)
                    return
                else:
                    current_node = current_node.right

    def search(self, find_val):
        if self.root is None:
            return False

        current_node = self.root

        while current_node:
            if current_node.value == find_val:
                return True
            elif current_node.value > find_val:
                current_node = current_node.left
            else:
                current_node = current_node.right

        return False


# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)
