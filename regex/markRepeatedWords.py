#Author: ahmelq -  github.com/ahmedelq/
#License: MIT
#This is a solution of https://callumacrae.github.io/regex-tuesday/challenge1.html

def frw(msg):
    """finds and replaces repeated words with word_1 <strong>word_2</strong>"""
    import re
    return re.sub(r'\b(\S+)\s(\1)\b', 
                  r'\1 <strong>\2</strong>', 
                  msg, 
                  flags=re.I)

if __name__ == "__main__":
    test_cases = ["This is is a test", "This test test is is", "cat dog dog cat dog", "This is IS a test", "I'll I'll be be back back in in a a bit bit"]
    for txt in test_cases:
        print(frw(txt))