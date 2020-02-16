"""
pythonによるビット演算。論理シフトと算術シフトはどちらも '>>' でやってくれるっぽい
"""


def repeat_arithmetic_shift(num, count):
    for i in range(count):
        num = num >> 1
    return num


def repeat_logical_shift(num, count):
    if count == 0:
        return num

    target = int(bin(~num), 2) if num < 0 else int(bin(num), 2)
    for i in range(count):
        target = target >> 1
    return target


def main():
    print(repeat_arithmetic_shift(num=-8, count=2))
    print(repeat_arithmetic_shift(num=-93242, count=40))

    print(repeat_logical_shift(num=-75, count=1))
    print(repeat_logical_shift(num=93242, count=40))


if __name__ == "__main__":
    main()
