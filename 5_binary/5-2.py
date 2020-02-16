import unittest


def convert_double_type_num_to_bid(num: float):
    if num >= 1 or num < 0:
        return "入力値は0以上1未満にしてください"
    ret = "0."

    while num > 0:
        if len(ret) > 32:
            return "ERROR"

        r = num * 2
        if r >= 1:
            ret += "1"
            num = r - 1
        else:
            ret += "0"
            num = r

    return ret


class TestConvertDoubleTypeNumToBid(unittest.TestCase):
    def test_it1(self):
        assert convert_double_type_num_to_bid(0.5) == "0.1"

    def test_it2(self):
        assert convert_double_type_num_to_bid(0.1) == "ERROR"

    def test_it3(self):
        assert convert_double_type_num_to_bid(10) == "入力値は0以上1未満にしてください"


if __name__ == "__main__":
    unittest.main()
