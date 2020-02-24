import unittest

from bid_operation import set_bit


def create_even_mask(num):
    """ 対象と同じ桁数で、偶数桁が1のmaskビットを作成する """
    num_bit_length = len(bin(num)) - 2
    mask = 0
    for i in range(1, num_bit_length + 1):
        if i % 2 == 0:
            mask = set_bit(mask, i)
    return mask


def create_odd_mask(num):
    """ 対象と同じ桁数で、奇数桁が1のmaskビットを作成する """
    num_bit_length = len(bin(num)) - 2
    mask = 0
    for i in range(1, num_bit_length + 1):
        if i % 2 != 0:
            mask = set_bit(mask, i)
    return mask


def exchange_even_odd(num):
    even_mask = create_even_mask(num)
    odd_mask = create_odd_mask(num)

    masked_even_num = num & even_mask
    masked_odd_num = num & odd_mask

    shifted_even = masked_even_num >> 1
    shifted_odd = masked_odd_num << 1
    return shifted_even | shifted_odd


class TestGetAdjacentNumbers(unittest.TestCase):
    def test_it1(self):
        """ ４(偶数)ビット """
        # 11(10) == "0b1011"
        assert exchange_even_odd(11) == int("0b0111", 2)

    def test_it2(self):
        """ 5(奇数)ビット """
        # 30(10) == "0b11110"
        assert exchange_even_odd(30) == int("0b101101", 2)


if __name__ == "__main__":
    unittest.main()
