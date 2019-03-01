#Author: ahmelq -  github.com/ahmedelq/
#License: MIT
#This is a solution of the challange: https://old.reddit.com/r/dailyprogrammer/comments/6jr76h/20170627_challenge_321_easy_talking_clock/

def getTimeInText(num_time):
    """given a military time xx:xx, it spits it as text """
    tm = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve"
    }
    import re
    ex_time = re.search('^(\d{2}):(\d{2})$', num_time,re.IGNORECASE)
    if ex_time:
        mil_hr = int(ex_time.group(1))
        isAmPm = "pm" if mil_hr > 12 else "am"
        txt_hr = tm.get(mil_hr)
        return "it's {} {}.".format(ex_time.group(txt_hr), ex_time.group(2))
    return tm.get()

if __name__ == "__main__":
    print(getTimeInText("hello"))