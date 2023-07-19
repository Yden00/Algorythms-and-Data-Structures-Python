
from converter import numeral_converter

def test_numeral_converter():
    # 0x10
    assert numeral_converter(123, 10) == '123'
    assert numeral_converter(0, 10) == '0'
    assert numeral_converter(4567, 10) == '4567'

    # 0x2
    assert numeral_converter(1101, 2) == '1101'
    assert numeral_converter(0, 2) == '0'
    assert numeral_converter(101010, 2) == '101010'

    # 0x16
    assert numeral_converter(0xFF, 16) == 'FF'
    assert numeral_converter(0, 16) == '0'
    assert numeral_converter(0x1A3, 16) == '1A3'

    print("Красавчик!")

if __name__ == '__main__':
    test_numeral_converter()




