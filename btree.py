# based on implementation from lesson

from queue import Queue


class LLBinaryTree:
    def __init__(self, root):
        self.key = root
        self.left = None
        self.right = None

    def insert_left(self, new_node):
        if self.left is None:
            self.left = LLBinaryTree(new_node)
        else:
            temp = LLBinaryTree(new_node)
            temp.left = self.left
            self.left = temp

    def insert_right(self, new_node):
        if self.right is None:
            self.right = LLBinaryTree(new_node)
        else:
            temp = LLBinaryTree(new_node)
            temp.right = self.right
            self.right = temp

    def get_right(self):
        return self.right

    def get_left(self):
        return self.left

    def get_leaves(self):
        lst = []

        def recursion(tree, lst):
            if tree.left is None and tree.right is None:
                lst.append(tree.key)
            else:
                if tree.left is not None:
                    recursion(tree.left, lst)
                if tree.right is not None:
                    recursion(tree.right, lst)

        recursion(self, lst)
        return lst
