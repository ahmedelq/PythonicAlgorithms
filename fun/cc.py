#Author: ahmelq -  github.com/ahmedelq/
#License: MIT
#This is a solution of the challange: https://www.reddit.com/r/dailyprogrammer/comments/pkw2m/2112012_challenge_3_easy/
def sc(txt, shft_amt=3, isDeq=False):
    """This is a chiper alg; given a text an a possible integer, it will shift the text 'shft_amt' """
    shft_amt *= (-1) ** isDeq
    result = ""
    for c in txt:
        new_chr = c
        if c.isalpha():
            ascii_chr = ord(c)
            new_ascii = ( (ascii_chr & 0x1F) + shft_amt ) % 26
            new_chr   = chr(new_ascii | ascii_chr & 96)
        result += new_chr
    return result


if __name__ == "__main__":
    txt = "Attack Mars at 13:37"
    print(sc(txt), "-->", sc(sc(txt), 3, True) )
