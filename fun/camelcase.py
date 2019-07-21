#Author: ahmelq -  github.com/ahmedelq/
#License: MIT
#This is a solution of the challange: https://www.codewars.com/kata/camelcase-method/python


def camel_case(string):
    return ''.join(
        w.title() for w in string.split()
    )

