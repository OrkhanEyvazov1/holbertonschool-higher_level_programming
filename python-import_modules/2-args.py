#!/usr/bin/python3
import sys
if len(sys.argv) == 1:
    print("0 arguments.")
elif len(sys.argv) == 2:
    print("1 argument:")
    print(sys.argv[1])
elif len(sys.argv) > 2:
    print("{} arguments:".format(
        len(sys.args)))
    for arg in sys.argv:
        if arg != sys.argv[0]:
            print("{}: arg".format(sys.argv.index(arg)))
