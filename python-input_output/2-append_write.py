#!/usr/bin/python3

''' doc '''


def append_write(filename="", text=""):
    """Function to append to a file"""
    with open("{}".format(filename), 'a', encoding="utf-8") as f:
        return f.write("{}".format(text))
