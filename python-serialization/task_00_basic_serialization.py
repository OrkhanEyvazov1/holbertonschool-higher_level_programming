#!/usr/bin/python3
''' serialization dict json module '''

import json


def serialize_and_save_to_file(data, filename):
    '''serialize data to json'''
    with open(filename, 'w', encoding='utf-8') as f:
            return json.dump(data, f)


def load_and_deserialize(filename):
    '''deserialize json'''
    with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
