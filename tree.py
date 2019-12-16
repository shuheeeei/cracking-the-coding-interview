class Node:
    def __init__(self, data):
        self.data = data
        self.left: Node = None
        self.right: Node = None


class Tree:
    def __init__(self, root):
        self.root: Node = root
