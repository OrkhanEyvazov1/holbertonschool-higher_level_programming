#!/usr/bin/python3
def reverse():
    i = 0
    for char_code in range(ord('z'), ord('a') - 1, -1):
        if i % 2 != 0:
            char_code -= 32
        print("{}".format(chr(char_code)), end="")
        i += 1


reverse()
