#Author: ahmelq -  github.com/ahmedelq/
#License: MIT
#This is a solution of https://www.codewars.com/kata/regex-validate-pin-code

def validatepin(pin):
    """returns true if the pin is digits only and has length of 4 or 6"""
    import re
    return bool(re.match("^(\d{6}|\d{4})$", pin))

if __name__ == "__main__":
    print("1234a", validatepin("1234a"))
    print("12345", validatepin("12345"))
    print("123456", validatepin("123456"))
    
    
    