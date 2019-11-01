from itertools import starmap 

def intirize(nl):
    return list(map(lambda x: int(x), list(nl)))

def solution():
    inpt = input().split()
    n = inpt[0]
    init_state = intirize(inpt[1] )
    key = intirize(inpt[2])
    fun = lambda x,y: min( abs(x - y), -abs(x - y) % 10 )
    return sum(starmap(fun, zip(init_state,key)))
    


print(solution())