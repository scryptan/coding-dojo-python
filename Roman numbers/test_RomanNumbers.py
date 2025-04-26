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

def test_int_to_roman_return_i_when_pass_1():
    assert 'I' == roman_numbers.int_to_roman(1)

def test_int_to_roman_return_iv_when_pass_4():
    res = roman_numbers.int_to_roman(4)
    print(f'\nactual: {res}')
    assert 'IV' == res

def test_int_to_roman_return_ix_when_pass_9():
    assert 'IX' == roman_numbers.int_to_roman(9)

def test_int_to_roman_return_xlix_when_pass_49():
    assert 'XLIX' == roman_numbers.int_to_roman(49)

def test_int_to_roman_return_xxxvii_when_pass_37():
    assert 'XXXVII' == roman_numbers.int_to_roman(37)

