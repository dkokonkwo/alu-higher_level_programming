#!/usr/bin/python3
"""creates class MyList that performs sorting function"""


class MyList(list):
    """defines my_sorted that returns a sorted list"""


    def print_sorted(self):
        """sorts lists in ascending order"""
        sorted(self)
        print(sorted(self))
