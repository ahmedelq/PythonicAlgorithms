
num = 600851475143
p = int(num**0.5) + 1
factors = []
def addToFactors(x):
    for f in factors:
        if not x % f:
            return
    factors.append(x)

for i in range(2, p):
    if not num % i: addToFactors(i)

print(max(factors))
