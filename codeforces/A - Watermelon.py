# -*- coding: utf-8 -*-

##################################################
## Author:  ahmelq
## License: MIT
## Github:  https://github.com/ahmedelq
## Status:  Solved
## Problem: https://codeforces.com/contest/4/problem/A
##################################################


def isWatermelon(w):
    for i in range(2, w, 2):
        if not ( (w - i) % 2 ):
            return 'YES'
    return 'NO'


for i in range(100):
    print(i, isWatermelon(i))