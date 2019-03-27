#Author: ahmelq -  github.com/ahmedelq/
#License: MIT
#this is a solution of https://old.reddit.com/r/dailyprogrammer/comments/aphavc/20190211_challenge_375_easy_print_a_new_number_by/

# -- coding: utf-8 --

def exoticNum(n):
    return ''.join([
             str(int(num) + 1)
             for num in list(str(n))])

if __name__ == "__main__":
    print(
        exoticNum(998)
    )