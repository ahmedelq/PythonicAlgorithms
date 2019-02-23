def binsearch(x, arry):
    hi = len(arry) - 1
    lo = 0 
    while hi >= lo: 
        pos = hi - lo // 2
        if x > arry[pos]: 
            lo = pos + 1
        elif x < arry[pos]:
            hi = pos - 1
        else:
            return pos
    return -1

if __name__ == "__main__":
    res = binsearch(-143, [1, 2, 5, 6, 9, 10, 13, 14, 16])
    print(res)