# An object that facilitates the traversal of a data structure

class Node:
    """
    Iterator Pattern: Represents a node in a binary tree.
    Provides a method for traversing the tree in preorder.
    """
    def __init__(self, value, left=None, right=None):
        """Initializes the node with a value, left child, and right child."""
        self.right = right
        self.left = left
        self.value = value

        self.parent = None

        if left:
          self.left.parent = self
        if right:
          self.right.parent = self

    def traverse_preorder(self):
        """
        Traverses the tree in preorder and returns a list of values.
        Uses an inner function for recursive traversal.
        """
        result = []
        def traverse(node):
            """Inner function for recursive preorder traversal."""
            if node:
                result.append(node.value)
                traverse(node.left)
                traverse(node.right)
        traverse(self)
        return result


if __name__ == '__main__':
    root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
    print(root.traverse_preorder()) # Output: [1, 2, 4, 5, 3, 6, 7]
