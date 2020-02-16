import unittest


def count_necessary_bit_conversion(num, target):
    """num1からnum2に変換するのに必要なビット数を返す """
    if num == target:
        return 0
    bin_num_len = len(bin(num))
    bin_target_len = len(bin(target))
    bin_target = bin(target)[2:]
    bin_num = bin(num)[2:]
    if bin_num_len > bin_target_len:
        bin_target = "0" * (bin_num_len - bin_target_len) + bin(target)[2:]
    else:
        num = num << (bin_num_len - bin_target_len)
        bin_num = bin(num)[2:]
    count = 0
    for n, t in zip(bin_num, bin_target):
        if n != t:
            count += 1
    return count


class TestNecessaryBitConversion(unittest.TestCase):
    def test_it1(self):
        assert count_necessary_bit_conversion(29, 15) == 2


if __name__ == "__main__":
    unittest.main()