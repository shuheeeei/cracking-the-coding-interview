import unittest


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.size = 0

    @classmethod
    def count_paths_with_sum(cls, root, target_num):
        if root is None:
            return 0

        paths_from_root = cls.count_paths_with_sum_from_node(root, target_num, 0)

        paths_on_left = cls.count_paths_with_sum(root.left, target_num)
        paths_on_right = cls.count_paths_with_sum(root.right, target_num)

        return paths_from_root + paths_on_left + paths_on_right

    @classmethod
    def count_paths_with_sum_from_node(cls, node, target_num, current_sum):
        if node is None:
            return 0

        current_sum += node.data

        total_paths = 0
        if current_sum == target_num:
            total_paths += 1

        total_paths += cls.count_paths_with_sum_from_node(node.left, target_num, current_sum)
        total_paths += cls.count_paths_with_sum_from_node(node.left, target_num, current_sum)
        return total_paths


class TestNewNode(unittest.TestCase):
    def test_get_random_node(self):
        root = Node(5)

        root.left = Node(2)
        root.right = Node(10)

        root.left.left = Node(1)
        root.left.right = Node(3)
        root.right.left = Node(7)
        root.right.right = Node(15)

        count = Node.count_paths_with_sum(root, 10)
        assert count == 1


if __name__ == "__main__":
    unittest.main()
