"""
部分木チェック：T1とT2は非常に大きい二分木で、T1はT2と比べてかなり大きくなっています。
              このとき、T2がT1の部分木であるかどうかを判定するアルゴリズムを作ってください。
"""

import unittest


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def insert(self, data):
        n = self
        # print("data", data)
        while n:
            if data <= n.data:
                # print("left:", data)
                if n.left is None:
                    n.left = Node(data)
                    break
                n = n.left
            elif data > n.data:
                # print("right:", data)
                if n.right is None:
                    n.right = Node(data)
                    break
                n = n.right
            else:
                n.data = Node(data)
                break

    @classmethod
    def is_contained(cls, t1, t2):
        string1 = cls.get_ordered_node(t1, [])
        print("string1", string1)
        string2 = cls.get_ordered_node(t2, [])
        print("string2", string2)

        return set(string2) < set(string1)

    @classmethod
    def get_ordered_node(cls, node, contents):
        """pre-orderでTreeをなぞってリストにいれて比較する"""
        if node is None:
            return
        contents.append(node.data)
        cls.get_ordered_node(node.left, contents)
        cls.get_ordered_node(node.right, contents)
        return contents


class TestIsContained(unittest.TestCase):
    def setUp(self) -> None:
        node_numbers = [2, 1, 3, 5, 6, 8, 18, 15, 20, 12, 17]
        self.root = Node(10)
        for data in node_numbers:
            self.root.insert(data)

    def test_true(self):
        node_numbers = [6, 8]
        root2 = Node(5)
        for data in node_numbers:
            root2.insert(data)
        assert Node.is_contained(self.root, root2)

    def test_false(self):
        node_numbers = [30000, 8000]
        root2 = Node(1000)
        for data in node_numbers:
            root2.insert(data)
        assert not Node.is_contained(self.root, root2)


if __name__ == "__main__":
    unittest.main()
