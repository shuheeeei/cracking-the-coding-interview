import unittest


def get_most_long_1bit_rows(num):
    bin_num = bin(num)[2:]
    if "0" not in bin_num:
        return len(bin_num)

    if num == 0:
        return 1

    max_candidates = list()
    len_1list = list(map(lambda x: len(x), bin_num.split("0")))
    for i in range(len(len_1list) - 1):
        max_candidates.append(len_1list[i] + len_1list[1 + 1])

    # 1ビット分を１に変換するので１足して返す
    return max(max_candidates) + 1


class TestGetMostLong1BidRows(unittest.TestCase):
    def test_it1(self):
        assert get_most_long_1bit_rows(1775) == 8

    def test_it2(self):
        assert get_most_long_1bit_rows(0) == 1

    def test_it3(self):
        assert get_most_long_1bit_rows(15) == 4


if __name__ == "__main__":
    unittest.main()
