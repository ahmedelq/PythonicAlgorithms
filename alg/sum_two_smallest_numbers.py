#Author: ahmelq -  github.com/ahmedelq/
#License: MIT
#This is a solution of the challange: https://www.codewars.com/kata/558fc85d8fd1938afb000014/train/python

def sum_two_smallest_numbers(numbers):
    numbers.sort()
    l = len(numbers)
    if l > 1:
        return numbers[0] + numbers[1]
    elif l > 0 :
        return numbers[0]
    else:
        return 0

if __name__ == "__main__":
    print(
        sum_two_smallest_numbers([5, 8, 12, 18, 22]) #13
    )