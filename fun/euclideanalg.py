#Author: ahmelq -  github.com/ahmedelq
#License: MIT

def euc(a,b):
    """givn two integers, prints the procedures to compute their greatest common divsor"""
    if a==0 or b==0:
        return 
    mx = max(a,b)
    mn = min(a,b)
    qt = mx // mn
    re = mx - (qt * mn)
    print(str(mx) +"="+ str(qt) +"("+ str(mn) +") + " + str(re))
    euc(mn, re)
    


if __name__ == "__main__":
    euc(3120,17)

