#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0

    roman_numeral = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100,
                     "D": 500, "M": 1000}
    subtractive_notation = {"IV": 4, "IX": 9, "XL": 40, "XC": 90,
                            "CD": 400, "CM": 900}
    value = 0
    i = 0

    while i < len(roman_string):
        s = ""
        if i < len(roman_string) - 1:
            s = roman_string[i] + roman_string[i + 1]

        if s in subtractive_notation:
            value += subtractive_notation[s]
            i += 2
        elif roman_string[i] in roman_numeral:
            value += roman_numeral[roman_string[i]]
            i += 1
        else:
            return 0
    return value
