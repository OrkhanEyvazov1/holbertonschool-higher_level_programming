#!/usr/bin/python3

import sys


def main():
    arg_count = len(sys.argv) - 1

    if arg_count == 0:
        print("0 arguments.")
    else:
        # F-string for cleaner pluralization
        plural = "s" if arg_count > 1 else ""
        print(f"{arg_count} argument{plural}:")

        # Iterate over arguments starting from index 1 (the first actual argument)
        # The '1' in enumerate ensures the numbering starts at 1, not 0.
        for i, arg in enumerate(sys.argv[1:], 1):
            # Print the correct argument value, not the literal string "arg"
            print(f"{i}: {arg}")


if __name__ == "__main__":
    main()
