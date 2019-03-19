#Author: ahmelq -  github.com/ahmedelq/
#License: MIT
#this is a solution of https://www.codewars.com/kata/find-the-parity-outlier/


def find_outlier(integers):
    out = list(map(lambda x: x % 2, integers))
    if out.count(1) > out.count(0):
        return integers[out.index(0)]
    else:
        return integers[out.index(1)]



print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))