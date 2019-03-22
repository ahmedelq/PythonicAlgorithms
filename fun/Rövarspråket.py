#Author: ahmelq -  github.com/ahmedelq/
#License: MIT
#this is a solution of https://www.reddit.com/r/dailyprogrammer/comments/341c03/20150427_challenge_212_easy_r%C3%B6varspr%C3%A5ket/

# -- coding: utf-8 --

def rov(txt):
    return ''.join([
        c + 'o' + c.lower()
        if c.isalpha() and c.upper() not in "A E I O U Y Å Ä Ö"
        else c
        for c in txt
    ])
    


print(
    rov("Jag talar Rövarspråket!"),
    rov("I'm speaking Robber's language!"),
    sep="\n"
    )