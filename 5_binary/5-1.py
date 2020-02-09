import unittest

from bid_operation import clear_bit


def modified_clear_bit(num, i):
    return bin(clear_bit(num, i))


def insert_bits(bid_n: str, bid_m: str, i: int, j: int):
    # i~jまでをclear_bidする。
    for idx in range(i, j + 1):
        bid_n = modified_clear_bit(int(bid_n, 2), idx)

    # i~jはbid_mでそれ以外を１にしたビットを作成する
    bid_n_length = len(bid_n) - 2
    mask = ("0b"
            + "0" * (bid_n_length - i - (j - i + 1))
            + bid_m[2:] + i * "0")
    # 元のビットと上記で作成したビットでorをとる
    return bin(int(bid_n, 2) | int(mask, 2))


class TestInsertBits(unittest.TestCase):
    def test_it1(self):
        assert insert_bits("0b10001111100", "0b10011", 2, 6) == "0b10001001100"


if __name__ == "__main__":
    unittest.main()
