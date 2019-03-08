#Author: ahmelq -  github.com/ahmedelq/
#License: MIT
#This is a solution of the challange: https://www.reddit.com/r/dailyprogrammer/comments/r8a70/3222012_challenge_29_easy/

def isPalindrome(txt):
    """Given a string, determine weather its a palindrome or not"""
    for i in range(len(txt)):
        if txt[i] != txt[-(i + 1)]:
            return False
    return True

def isPalindrome_2(txt):
    #inspired by /u/gjwebber, very elegent solution tbh :]
    return txt == txt[::-1]

if __name__ == "__main__":
    test_cases = [
        "123321", "haah", "hannah", "madam", "racecar", "10801",
        "man", "this", "is", "false"
    ] #some from wikipedia
    for tc in test_cases:
        print(tc, isPalindrome(tc))
