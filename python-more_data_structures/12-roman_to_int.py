#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = { "I" : 1, "V" : 5, "X" : 10, "C" : 100, "D" : 500, "M" : 1000}
    sum = 0
    for i in range(len(roman_string)-1):
            curr = roman[roman_string[i]]
            nexx = roman[roman_string[i+1]]
            if curr < nexx:
                sum -= curr
            else:
                sum += curr
    last_char_index = len(roman_string) - 1
    sum += roman[roman_string[last_char_index]]
    return sum
