class BTNode:
    def __init__(self, item):
        self.key = item
        self.right = None
        self.left = None

    def is_leaf(self):
        if self.right is None and self.left is None:
            return True
        return False
