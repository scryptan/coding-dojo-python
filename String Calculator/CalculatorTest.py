import Calculator

calc = Calculator.Calculator()

def test_class_is_working():
    assert 'some str' == calc.test()

def test_add_empty_returns_0():
    assert calc.add("") == 0

def test_add_one_number_should_return_it():
    assert calc.add("1") == 1

def test_add_two_numbers_returns_sum():
    assert calc.add("1,2") == 3

def test_add_two_numbers_with_space_returns_sum():
    assert calc.add("1,2 ") == 3