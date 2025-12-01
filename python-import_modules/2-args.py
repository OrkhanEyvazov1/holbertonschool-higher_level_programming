#!/usr/bin/python3
import sys
def main():
    arg_count = len(sys.argv) - 1
    if arg_count == 0:
        print("0 arguments.")
    else:
        plural = "s" if arg_count > 1 else ""
        print(f"{arg_count} argument{plural}:")
        for i, arg in enumerate(sys.argv[1:], 1):
            print(f"{i}: {arg}")
if __name__ == "__main__":
    main()
