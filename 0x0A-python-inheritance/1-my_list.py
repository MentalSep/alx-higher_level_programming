#!/usr/bin/python3
""" Module that contains MyList class """


class MyList(list):
    """ Class that inherits from list """

    def print_sorted(self):
        """ Method that prints the list, but sorted (ascending sort) """
        print(sorted(self))
