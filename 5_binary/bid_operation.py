def get_bit(num, i) -> bool:
    """ 1→True, 0→False """
    return (num & 1 << i) != 0


def set_bit(num, i) -> int:
    """ i番目を１にSETする"""
    return num | 1 << i


def clear_bit(num, i) -> int:
    num_len = len(bin(num)) - 2
    mask_bit = (["1"] * (num_len - 1))
    mask_bit.insert(num_len-1-i, "0")
    mask = "0b" + "".join(mask_bit)
    return num & int(mask, 2)


def bit_reverse(num):
    num_len = len(bin(num)) - 2  # "0b"は除く
    mask = 2 ** num_len - 1  # 0乗目からのスタートなので１を引く
    return bin(num ^ mask)


def clear_bits_msb_through_i(num, i):
    mask = int(bit_reverse(1 << i), 2) - 1
    return num & mask


def clear_bits_i_through_0(num, i):
    mask = int(bit_reverse(1 << i), 2) - 1
    return num & mask


def update_bit(num, i):
    value = 1 if get_bit(num, i) else 0
    num_len = len(bin(num)) - 2
    mask_bit = (["1"] * (num_len - 1))
    mask_bit.insert(num_len-1-i, "0")
    mask = "0b" + "".join(mask_bit)
    return (num * int(mask, 2)) | (value << i)


def main():
    print(bin(10))
    # print(get_bit(num=10, i=1))
    # print(set_bit(num=10, i=0))
    print(clear_bit(num=10, i=3))
    # print(clear_bits_msb_through_i(num=10, i=2))


if __name__ == "__main__":
    main()
