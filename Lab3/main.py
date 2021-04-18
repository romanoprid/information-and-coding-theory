def main():
    dec_combination = 794

    print(f'Binary form of {dec_combination} is {bin(dec_combination)}')

    print('Coding:')
    gray = coding(dec_combination)
    print(f'Number {bin(dec_combination)} converted to Gray code: {bin(gray)}')

    print('Decoding:')
    binary = decoding(gray)
    print(f'Number in Gray code {bin(gray)} converted to binary: {bin(binary)}')


def coding(number):
    """Converts binary to Gray code"""
    if isinstance(number, str):
        number = int(number, 2)

    return number ^ (number >> 1)


def decoding(number):
    """Converts Gray code to binary"""
    if isinstance(number, str):
        number = int(number, 2)

    mask = number >> 1

    while mask:
        number ^= mask
        mask >>= 1

    return number


if __name__ == '__main__':
    main()
