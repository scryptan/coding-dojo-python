import pytest

from RomanNumbers import RomanNumbers

roman_numbers = RomanNumbers()


def test_alive():
    assert True


def test_int_to_roman_raise_exception_when_negative():
    with pytest.raises(ValueError) as excinfo:
        roman_numbers.int_to_roman(-1)

    assert "Number must be between 1 and 3999" == str(excinfo.value)


def test_int_to_roman_raise_exception_when_bigger_than_3999():
    with pytest.raises(ValueError) as excinfo:
        roman_numbers.int_to_roman(4000)

    assert "Number must be between 1 and 3999" == str(excinfo.value)


@pytest.mark.parametrize("input, expected", [
    (1, 'I'),
    (4, 'IV'),
    (9, 'IX'),
    (49, 'XLIX'),
    (37, 'XXXVII')
])
def test_int_to_roman_return_i_when_pass_1(input, expected):
    assert expected == roman_numbers.int_to_roman(input)
