#1 1 2 3 5 8 13...
#1 2 3 4 5 6 7...

def fib(n):
    """spits Fib_n value """ 
    # operates in O(n), storage in O(1)
    c=1 #c = current
    p=c #p = previous
    for _ in range(n - 2):
        tmp = c
        c += p
        p = tmp
    return c

if __name__ == "__main__":
    print(
        "{} = {}".format("fib(7)", fib(7))
    )