#Author: ahmelq -  github.com/ahmedelq/
#License: MIT
#This is a solution of the challange: https://codegolf.stackexchange.com/questions/180970/create-chunks-from-an-array?page=2&tab=votes#tab-top

def split(ary, n):
    """Given an array, and an integer, split the array into n parts"""
    result = []
    for i in range(0, len(ary), n):
        result.append(ary[i: i + n])
    return result


if __name__ == "__main__":
    a = [1,2,3,4,5,6]
    print(
    split(a, 2),
    split(a, 3),
    split(a, 4)
    )