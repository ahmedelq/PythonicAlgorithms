#Author: ahmelq -  github.com/ahmedelq
#License: MIT

def compareTriplets(a, b):
    """Rate two tuples, if a[i] > b[i] give a 1 point, b[i] > a[i] give b 1 point, give 0 otherwise"""
    cmp = lambda x,y: x > y
    return [sum(map(cmp, a,b)), sum(map(cmp, b, a))]

def compareTripletsSFW(a, b):
    """Same as compareTriplets, implemented strightforwardlly"""
    result = [0, 0]
    for i in range(min(len(a), len(b))):
        if a[i] > b[i]:
            result[0] = result[0] + 1
        elif b[i] > a[i]:
            result[1] = result[1] + 1
    return result 


if __name__ == "__main__":
    a = (5, 6, 7)
    b = (3, 6, 10)
    print("functional:", compareTriplets(a, b))
    print("SFW:", compareTripletsSFW(a, b))
    