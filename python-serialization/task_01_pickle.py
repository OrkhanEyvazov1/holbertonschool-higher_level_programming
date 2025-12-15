#!/usr/bin/python3
'''docstring'''


import pickle


class CustomObject:
    '''Class docstring'''

    def __init__(self, name, age, is_student):
        '''Initializer docstring'''
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        '''Display method docstring'''
        print(f'Name: {self.name}\n, Age: {self.age}\n, Is Student: {self.is_student}')

    def serialize(self, filename):
        '''Serialize method docstring'''
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        '''Deserialize method docstring'''
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.UnpicklingError, EOFError):
            return None
