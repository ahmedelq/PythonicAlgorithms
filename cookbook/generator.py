
def get_even_numbers(start=0, end=10):
    for i in range(start, end):
        if i % 2 == 0:
            yield i


a = get_even_numbers()
print(next(a)) # first item exhausted 
print(list(a))

def fib(n):
    """
    Fibonacci function using a generator
    """
    a, b = 0,1
    for _ in range(n):
        a,b = b, b + a
        yield a  


print(list(fib(10)))