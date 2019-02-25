#Author: ahmelq -  github.com/ahmedelq
#License: MIT

def iss(ary):
    """Sorts an array in a nondecreasing order""" 
    ary_len = len(ary)
    for i in range(ary_len):
        j = i
        while ary[j] < ary[j - 1] and j > 0:
            ary[j], ary[j - 1] = ary[j - 1], ary[j]
            j -= 1
    return ary

if __name__ == "__main__":
    ary = [5, 6, 2, 4, 1, 3, 1]
    print("Array before:", ary)
    print("Insertion sort:", iss(ary))