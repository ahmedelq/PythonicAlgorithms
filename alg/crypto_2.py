#Author: ahmelq -  github.com/ahmedelq/
#License: MIT
#This is a solution of the challange: https://www.codewars.com/kata/encrypt-this/python

def encrypt_this(text):
    text = text.split()
    res = []
    for word in text:
        n = len(word)
        f = ord(word[0])
        if n == 1:
            res.append(str(f))
        elif n == 2:
            res.append("{}{}".format(f, word[1]))
        else:
          s = word[1:2-n]
          m = word[2-n:n-1]
          e = word[n-1:n]
          res.append("{}{}{}{}".format(f, e, m, s))
    return ' '.join(res)


if __name__ == "__main__":
    print(encrypt_this("A wise old owl lived in an oak"))