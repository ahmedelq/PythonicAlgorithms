#Author: ahmelq -  github.com/ahmedelq/
#License: MIT

from functools import reduce
def arysum(ary):
    """Given a numerical array, it returns the array sum""" 
    return reduce(lambda a,b: a + b, ary)

if __name__ == "__main__":
    some_array = [1, 2, 3, 4, 5]
    print("The sum of", some_array, "is", arysum(some_array))
