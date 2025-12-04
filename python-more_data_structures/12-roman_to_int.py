#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0

    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    total = 0
    for i in range(len(roman_string) - 1):
        curr = roman.get(roman_string[i], 0)
        nxt = roman.get(roman_string[i + 1], 0)

        if curr < nxt:
            total -= curr
        else:
            total += curr

    total += roman.get(roman_string[-1], 0)
    return total
