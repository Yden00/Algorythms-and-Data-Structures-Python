
from converter import numeral_converter

def test_numeral_converter():

    # 0x2
    assert numeral_converter(10, 2) == "1010"
    assert numeral_converter(43, 2) == "101011"
    assert numeral_converter(17, 2) == "10001"

    # 0x8
    assert numeral_converter(123, 8) == "173"
    assert numeral_converter(64, 8) == "100"
    assert numeral_converter(512, 8) == "1000"

    # 0x16
    assert numeral_converter(255, 16) == "FF"
    assert numeral_converter(1024, 16) == "400"
    assert numeral_converter(4096, 16) == "1000"

    # 0x10
    assert numeral_converter(12345, 10) == "12345"
    assert numeral_converter(9876543210, 10) == "9876543210"
    assert numeral_converter(67890, 10) == "67890"

    #0x0
    assert numeral_converter(0, 16) == "0"
    assert numeral_converter(0, 2) == "0"
    assert numeral_converter(0, 8) == "0"

    try:
        numeral_converter(-10, 2)
    except ValueError:
        pass
    else:
        raise AssertionError("Тут должна была быть ошибка ValueError, так как отрицательные числа нельзя")

    print("Красавчик!")

if __name__ == '__main__':
    test_numeral_converter()




