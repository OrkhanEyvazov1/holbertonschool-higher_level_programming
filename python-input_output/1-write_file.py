#!/usr/bin/python3

''' write '''


def write_file(filename="", text=""):
    """Function to read and print file"""
    with open("{}".format(filename), 'w', encoding="utf-8") as f:
        return f.write("{}".format(text))
