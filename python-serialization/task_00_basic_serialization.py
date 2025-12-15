#!/usr/bin/python3
''' serialization dict json module '''


def serialize_and_save_to_file(data, filename):
    '''serialize data to json'''
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    '''deserialize json'''
    with open(filename, 'r') as file:
        json.load(file)
