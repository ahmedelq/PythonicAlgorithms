#Author: ahmelq -  github.com/ahmedelq/
#License: MIT
#This is a solution of the challange: https://www.reddit.com/r/dailyprogrammer/comments/6v29zk/170821_challenge_328_easy_latin_squares/

"""
0 1 2 3 4 5 6 7 8

0 1 2 
3 4 5
6 7 8
"""
def isLatinSquare(aryLen, content):
    content = content.split()
    validList = content[:aryLen]
    for i in range(aryLen**2):
        pass



if __name__ == "__main__":
    print(
        isLatinSquare(
            int(input('The length of the array: ')),
            input('The content: ')
        )
    )