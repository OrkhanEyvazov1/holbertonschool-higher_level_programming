#!/usr/bin/python3
'''
inherit from list
'''


class MyList(list):
    ''' cls '''

    def __init__(self, *args):
        '''init'''
        super().__init__(args)

    def print_sorted(self):
        ''' print sorted list'''
        print(sorted(self))
