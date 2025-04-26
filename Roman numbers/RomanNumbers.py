class RomanNumbers:
    def __init__(self):
        self.roman_numerals = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M'
        }

    def int_to_roman(self, num: int) -> str:
        if not (0 < num < 4000):
            raise ValueError("Number must be between 1 and 3999")

        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]

        roman_numeral = ""
        for i in range(len(val)):
            count = num // val[i]
            roman_numeral += syms[i] * count
            num -= val[i] * count
        return roman_numeral
