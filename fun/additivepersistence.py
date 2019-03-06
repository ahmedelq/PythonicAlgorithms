#Author: ahmelq -  github.com/ahmedelq/
#License: MIT
#This is a solution of the challange: https://www.reddit.com/r/dailyprogrammer/comments/akv6z4/20190128_challenge_374_easy_additive_persistence/

def ap(n):
    counter = 0
    while n > 9 : 
        temp_n = n
        new_n  = 0

        while temp_n !=0 :
            new_n += temp_n % 10
            temp_n //= 10

        counter += 1
        n = new_n
    return counter


if __name__ == "__main__":
   print(ap(13), ap(1234), ap(9876),  ap(199), sep="\n")


