class Tree:
    def __init__(self, root):
        self.key = root
        self.children = []

    def add_child(self, item):
        self.children.append(Tree(item))

    def leaves(self):
        lst = []
        def recursion(tree, lst):
            if not tree.children:
                lst.append(tree)
            else:
                for i in tree.children:
                    recursion(i, lst)
        recursion(self, lst)
        return lst