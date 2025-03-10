# An object that facilitates the traversal of a data structure

class Node:
    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value

        self.parent = None

        if left:
          self.left.parent = self
        if right:
          self.right.parent = self

    def traverse_preorder(self):
        result = []
        def traverse(node):
            if node:
                result.append(node.value)
                traverse(node.left)
                traverse(node.right)
        traverse(self)
        return result


if __name__ == '__main__':
    root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
    print(root.traverse_preorder())
