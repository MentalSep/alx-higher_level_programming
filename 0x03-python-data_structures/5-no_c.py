#!/usr/bin/python3
def no_c(my_string):
    newString = ''
    for char in my_string:
        if char not in 'Cc':
            newString += char
    return newString
