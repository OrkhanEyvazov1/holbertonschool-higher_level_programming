#!/usr/bin/python3
printed_count = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            printed_count += 1
        except IndexError:
            break
    return printed_count
