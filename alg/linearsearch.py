def linsearch(x, arr):
    ary_len = len(arr)
    for i in range(ary_len):
        if x == arr[i]:
            return i
    return -1


if __name__ == "__main__":
    ary = [5, 3, 2, 9, 0, 1, 3, 4]
    print(linsearch(9, ary))
    print(linsearch(19, ary))
    