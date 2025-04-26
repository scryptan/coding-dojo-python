Конечно! Римские числа (Roman Numerals) представляются с помощью набора символов: I, V, X, L, C, D и M. Каждый символ представляет определенное десятичное значение:

- I = 1
- V = 5
- X = 10
- L = 50
- C = 100
- D = 500
- M = 1000

В римской системе чисел используются комбинации этих символов для представления различных чисел. Например:

- II = 2 (I + I)
- IV = 4 (V - I)
- IX = 9 (X - I)
- XL = 40 (L - X)
- XC = 90 (C - X)
- CD = 400 (D - C)
- CM = 900 (M - C)

### Примеры кода на Python

1. **Конвертация из римских чисел в десятичные**

```python
def roman_to_decimal(roman):
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    decimal = 0
    prev_value = 0
    
    for char in reversed(roman):
        value = roman_dict[char]
        if value < prev_value:
            decimal -= value
        else:
            decimal += value
        prev_value = value
    
    return decimal

# Пример использования
print(roman_to_decimal("MCMXCIV"))  # Выведет: 1994
```

2. **Конвертация из десятичных чисел в римские**

```python
def decimal_to_roman(decimal):
    roman_dict = [
        (1000, 'M'), 
        (900, 'CM'), 
        (500, 'D'), 
        (400, 'CD'),
        (100, 'C'), 
        (90, 'XC'), 
        (50, 'L'), 
        (40, 'XL'),
        (10, 'X'), 
        (9, 'IX'), 
        (5, 'V'), 
        (4, 'IV'),
        (1, 'I')
    ]
    
    roman = ''
    
    for value, symbol in roman_dict:
        while decimal >= value:
            roman += symbol
            decimal -= value
    
    return roman

# Пример использования
print(decimal_to_roman(1994))  # Выведет: MCMXCIV
```

Эти функции позволяют вам легко конвертировать числа между римской и десятичной системами счисления.
