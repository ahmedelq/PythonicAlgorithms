#Author: ahmelq -  github.com/ahmedelq/
#License: MIT
#This is a solution of the challange: https://www.reddit.com/r/dailyprogrammer/comments/afxxca/20190114_challenge_372_easy_perfectly_balanced/

def balanced(txt):
    """
   Given a string containing only lowercase letters, 
   find whether every letter that appears in the string appears the same number of times.
    """
    if len(txt) <= 1: return True
    from functools import reduce
    count_txt = dict() #same as using the Counter class from collections lib.
    for char in txt:
        count_txt[char] = count_txt.get(char, 0) + 1
    return reduce(lambda x,y: x==y, count_txt.values())


if __name__ == "__main__":
    print(
        balanced("xxxyyy"), #T
        balanced("yyyxxx"), #T
        balanced("xxxyyyy"), #F
        balanced("yyxyxxyxxyyyyxxxyxyx"), #T
        balanced("xyxxxxyyyxyxxyxxyy"), #F
        balanced(""), #T
        balanced("x"), #T

        sep="\n"
    )