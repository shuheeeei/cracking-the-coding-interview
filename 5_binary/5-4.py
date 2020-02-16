from collections import Counter
import unittest


def get_adjacent_numbers(num):
    """２進表記した時に１の数が同じなる隣接する数値を返す """
    bin_num = bin(num)[2:]
    if "1" not in bin_num:
        return None

    next_num = num + 1
    prev_num = num - 1

    num_of_1 = Counter(bin_num)["1"]
    # 1つ上の数を探す
    while num_of_1 != Counter(bin(next_num)[2:])["1"]:
        next_num += 1

    # 1つ下の数を探す
    if not num <= 1:
        while num_of_1 != Counter(bin(prev_num)[2:])["1"]:
            prev_num -= 1
    else:
        prev_num = None

    return prev_num, next_num


class TestGetAdjacentNumbers(unittest.TestCase):
    def test_it1(self):
        assert get_adjacent_numbers(10) == (9, 12)

    def test_it2(self):
        assert get_adjacent_numbers(1) == (None, 2)


if __name__ == "__main__":
    unittest.main()
