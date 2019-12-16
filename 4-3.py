"""
二分探索木が与えられた時、同じ深さのノード同士の連結リストを作るアルゴリズムを設計してください。
例えば、深さDの木がある時、D個の連結リストができます。
LinkedListが死んだのでpythonのlistを使ってますごめんさない許してください。
"""

import unittest
from collections import defaultdict

from linked_list import LinkedList
from tree import Node


def divide_by_depth(node, holder, depth):
    if not node:
        return holder
    depth += 1
    holder[f"depth{depth}"].append(node)
    divide_by_depth(node.left, holder, depth)
    divide_by_depth(node.right, holder, depth)
    return holder


class TestDivideByDepth(unittest.TestCase):
    def test_simple(self):
        root = Node(5)

        root.left = Node(2)
        root.right = Node(10)

        root.left.left = Node(1)
        root.left.right = Node(3)
        root.right.left = Node(7)
        root.right.right = Node(15)

        actual = divide_by_depth(root, defaultdict(list), 0)
        assert [a.data for a in actual["depth1"]] == [5]
        assert [a.data for a in actual["depth2"]] == [2, 10]
        assert [a.data for a in actual["depth3"]] == [1, 3, 7, 15]


if __name__ == "__main__":
    unittest.main()
