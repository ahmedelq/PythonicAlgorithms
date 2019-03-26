#Author: ahmelq -  github.com/ahmedelq/
#License: MIT
#this is a solution of https://www.reddit.com/r/dailyprogrammer/comments/1ystvb/022414_challenge_149_easy_disemvoweler/

def disemvowler(txt):
    vowels = ['a', 'e', 'i', 'u','o']
    phrase = ''
    extracted_vowels = ''
    txt = txt.replace(' ', '')
    for c in txt:
        if c not in vowels:
            phrase += c
        else:
            extracted_vowels += c   
    return phrase, extracted_vowels 

if __name__ == "__main__":
    print(
    disemvowler("two drums and a cymbal fall off a cliff"),
    disemvowler("all those who believe in psychokinesis raise my hand"),
    disemvowler("did you hear about the excellent farmer who was outstanding in his field")
    )