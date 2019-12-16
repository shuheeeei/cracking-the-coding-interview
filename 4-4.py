"""
平衡チェック：
二分木が平衡かどうかを調べる関数を実装してください。
平衡木とは、すべてのノードが持つ2つの部分木について、高さの差が１以下であるような木であると定義します
"""

import unittest
from collections import defaultdict

from linked_list import LinkedList
from tree import Node


class NewNode(Node):
    def has_child(self):
        return self.left or self.right


def is_equilibrium(binary_tree: NewNode) -> bool:
    if binary_tree.left and binary_tree.right is None:
        if binary_tree.left.has_child:
            return False
    if binary_tree.right and binary_tree.left is None:
        if binary_tree.right.has_child:
            return False

    if binary_tree.left is None and binary_tree.right is None:
        return True
    is_equilibrium(binary_tree.right)
    is_equilibrium(binary_tree.left)
    return True


class TestIsEquilibrium(unittest.TestCase):
    def test_true1(self):
        """ 高さの差が０ """
        root = NewNode(5)

        r_left = NewNode(2)
        root.left = r_left
        r_right = NewNode(10)
        root.right = r_right

        r_left.left = NewNode(1)
        r_left.right = NewNode(3)
        r_right.left = NewNode(7)
        r_right.right = NewNode(15)

        assert is_equilibrium(root) is True

    def test_true2(self):
        """ 高さの差が1 """
        root = NewNode(5)

        r_left = NewNode(2)
        root.left = r_left
        r_right = NewNode(10)
        root.right = r_right
        r_left.left = NewNode(1)

        assert is_equilibrium(root) is True

    def test_false(self):
        root = NewNode(5)

        r_left = NewNode(2)
        root.left = r_left
        r_left.left = NewNode(10)

        assert is_equilibrium(root) is False


if __name__ == "__main__":
    unittest.main()
