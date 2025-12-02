#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)

    if length==0:
        first = None
        return print("Length: {:d} - First character: {}".format(length, first))
    else:
        first = sentence[0]
        return print("Length: {:d} - First character: {}".format(length, first))
