#Author: ahmelq -  github.com/ahmedelq
#License: MIT

def ss(ary):
    """Sorts an array in a nondecreasing order""" 
    ary_len = len(ary)
    for i in range(ary_len):
        mn_val = ary[i]
        mn_indx = i
        for j in range(i + 1, ary_len):
            if ary[j] < mn_val:
                mn_val = ary[j]
                mn_inx = j
                ary[i], ary[j] = ary[j], ary[i]
    return ary


if __name__ == "__main__":
    ary = [5, 6, 2, 4, 1, 3, 1]
    print("Array before:", ary)
    print("Selection sort:",ss(ary))
