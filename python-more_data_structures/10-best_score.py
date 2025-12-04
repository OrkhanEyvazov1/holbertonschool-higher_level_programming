#!/usr/bin/python3

def best_score(a_dictionary):

    if not a_dictionary:
        return None
    first_key = next(iter(a_dictionary))
    best_key = first_key
    max_score = a_dictionary[first_key]
    for k, w in a_dictionary.items():
        if w > max_score:
            max_score = w
            best_key = k
    return best_key
