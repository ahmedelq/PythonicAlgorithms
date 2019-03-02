#Author: ahmelq -  github.com/ahmedelq/
#License: MIT
#This is a solution of the challange: https://nbviewer.jupyter.org/github/donnemartin/interactive-coding-challenges/blob/master/arrays_strings/unique_chars/unique_chars_challenge.ipynb

def isUniqueWithSet (str):
    """Given a string, checks if the string has unique charachters"""
    return len(set(str)) == len(str)

def isUniqueSFW(str):
    """
    Given a string, checks if the string has unique charachters
    Note that this solution is inefficient as it takes O(n^2)
    """
    l = len(str)
    for i in range(l):
        for j in range(l):
            if i != j and not ord(str[i]) ^ ord(str[j]):
                return False
    return True

if __name__ == "__main__":
    print(isUniqueSFW('bar')) # returns True
    print(isUniqueSFW('fool')) # returns False
    