
def sof(n):
    nums = set(range(2, n+1))
    for p in range(2,n):
        nums = nums.difference( range(2*p, n+1, p) )

    return nums


res = sof(100)
print ( sorted(list(res)), len(res))

