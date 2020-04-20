# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
# https://projecteuler.net/problem=1

# 1, 5, 10, 15, 20, ...
# 3, 6, 9, 12, 15, 18, 21, ...
limit = 1000


print( sum( set(range(5,limit,5)).union(set(range(3,limit,3))) ) )