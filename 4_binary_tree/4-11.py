import random
import unittest


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.size = 0

    def get_random_node(self):
        left_size = 0 if self.left is None else self.left.size
        idx = random.randint(1, self.size) if self.size else 0
        if idx < left_size:
            return self.left.get_random_node()
        elif idx == left_size:
            return self
        else:
            return self.right.get_random_node()

    def insert(self, entry):
        if self.data >= entry:
            if self.left is None:
                self.left = Node(entry)
            else:
                self.left.insert(entry)
        else:
            if self.right is None:
                self.right = Node(entry)
            else:
                self.right.insert(entry)
        self.size += 1

    def find(self, data):
        if self.data == data:
            return self
        elif self.data <= data:
            if self.right:
                return self.right.find(data)
            else:
                return
        elif self.data > data:
            if self.left:
                return self.left.find(data)
            else:
                return
        return None


class TestNewNode(unittest.TestCase):
    def setUp(self) -> None:
        self.node_numbers = [2, 1, 3, 5, 6, 8, 18, 15, 20, 12, 17]
        self.root = Node(10)
        for data in self.node_numbers:
            self.root.insert(data)

    def test_get_random_node(self):
        actual = self.root.get_random_node()

        assert isinstance(actual, Node)
        assert actual.data in self.node_numbers

    def test_find(self):
        target_num = 6
        actual = self.root.find(target_num)

        assert isinstance(actual, Node)
        assert actual.data == target_num


if __name__ == "__main__":
    unittest.main()
