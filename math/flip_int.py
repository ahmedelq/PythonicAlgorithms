def flip_int(n):
    """Given an integer n=x_1*10^0+...+x_n+1*10^n it will return 
    another integer in the form x_n+1*10^0+...+x_1*10^n"""
    res = n % 10
    n //= 10
    while n % 10:
        res *= 10 
        res += n % 10
        n //= 10
    return res 
        