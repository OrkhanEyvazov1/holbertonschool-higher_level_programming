#!/usr/bin/python3
print("{}".format("".join(
    chr(i) for i in range(ord('a'), ord('z') + 1)
    if i != ord('q') and i != ord('e')
)), end="")
