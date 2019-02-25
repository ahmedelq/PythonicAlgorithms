#Author: ahmelq -  github.com/ahmedelq
#License: MIT

def compareTriplets(a, b):
    """Rate two tuples, if a[i] > b[i] give a 1 point, b[i] > a[i] give b 1 point, give 0 otherwise"""
    cmp = lambda x,y: x > y
    return [sum(map(cmp, a,b)), sum(map(cmp, b, a))]


if __name__ == "__main__":
    a = (5, 6, 7)
    b = (3, 6, 10)
    print(compareTriplets(a, b))