class BTNode:
    """ Class for binary tree node representation. """

    def __init__(self, item):
        """
        (BTNode) -> NoneType
        Create new binary tree node.
        """
        self.key = item
        self.right = None
        self.left = None
