#Author: ahmelq -  github.com/ahmedelq/
#License: MIT
#This is a solution of the challange: https://www.reddit.com/r/dailyprogrammer/comments/pih8x/easy_challenge_1/
FILE_NAME = "usernames.txt"
 
def appendToFile(txt):
    with open(FILE_NAME, "a") as txtfile:
        txtfile.write(txt)
        txtfile.close()

def getUserInfo():
    prompt_mgs = ["What is your real name ?","How old are you",  "What is your reddit username ?"]
    uipt = []
    for msg in prompt_mgs:
        usr_inpt = input(msg + " ")
        while len(usr_inpt) < 1 :
            print("Invalid input, ")
            usr_inpt = input(msg)
        uipt.append(usr_inpt)
    return 'Your name is {}, you are {} years old, and your username is {}'.format(*uipt)
    


if __name__ == "__main__":
    txt = getUserInfo()
    appendToFile(txt)
    print(txt)