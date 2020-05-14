#Author: ahmelq -  github.com/ahmedelq
#License: MIT

def bubble_sort(ary):
    """Sorts an array in a nondecreasing order""" 
    for i in range(len(ary)):
        for j in range(len(ary) - 1):
            if ary[j] > ary[j + 1]: ary[j + 1], ary[j] = ary[j], ary[j + 1]
    return ary

if __name__ == "__main__":
    ary = [5, 6, 2, 4, 1, 3, 1]
    print("Array before:", ary)
    print("Insertion sort:", bubble_sort(ary))