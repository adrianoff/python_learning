class Node:
    def __init__(self, value=None, parent=None, left=None, right=None):
        self.right = right
        self.left = left
        self.parent = parent
        self.value = value


class BinTree:
    def __init__(self, root: Node):
        self.root = root


