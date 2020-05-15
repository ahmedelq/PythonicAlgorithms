#Author: ahmelq -  github.com/ahmedelq
#License: MIT

def bubble_sort(ary):
    """Sorts an array in a nondecreasing order""" 
    for i in range(len(ary), -1, -1):
        for j in range(i - 1):
            if ary[j] > ary[j + 1]: ary[j + 1], ary[j] = ary[j], ary[j + 1]
    return ary

if __name__ == "__main__":
    ary = [5, 6, 2, 7, 0, 4, 1, 3, 0, 1, 0]
    print("Before sorting:", ary)
    print("Bubble sort:", bubble_sort(ary))