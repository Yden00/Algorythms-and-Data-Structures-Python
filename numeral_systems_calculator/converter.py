

def numeral_converter(number: int, base: int = 10) -> str:
    dickt = {8: oct(number), 2: bin(number), 16: hex(number).upper(), 10: 'aa' + str(number)}
    return dickt[base][2:] if number >= 0 else int('asd')


if __name__ == '__main__':
    number, base = int(input()), int(input())
    print(numeral_converter(number, base))
