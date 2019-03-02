#Author: ahmelq -  github.com/ahmedelq/
#License: MIT
#This is a solution of the challange: https://old.reddit.com/r/dailyprogrammer/comments/6jr76h/20170627_challenge_321_easy_talking_clock/
def parseHour(hr):
    """returns a textual form of a military hour""" 
    return [
       'twelve', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
        'nine', 'ten', 'eleven'
            ][int(hr) % 12]
def parseMinutes(mn):
        """returns a textual form of minutes"""
        mn = list(map(lambda x: int(x), mn))
        fp = ['oh', '', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty'][mn[0]]
        sp = ['','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'][mn[1]]
        result = "{} {}".format(fp * (not mn[0]==mn[1]== 0), sp)
        if mn[0] == 1:
           result = ['ten', 'elevn', 'twelve', 'thirteen', 'fourteen','fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'][mn[1]]
        return result


def getTimeInText(num_time):
    """given a military time assumend as xx:xx, it spits it as text """
    import re
    ex_time = re.search('^(\d{2}):(\d{2})$', num_time,re.IGNORECASE)
    if ex_time:
        mil_hr = ex_time.group(1)
        isNight = "pm" if mil_hr > "12" else "am"
        txt_hr = parseHour(mil_hr); txt_min = parseMinutes(ex_time.group(2))
        return "it's {} {} {} {}.".format(txt_hr, "", txt_min, isNight)

if __name__ == "__main__":
    for i in range(24):
        for j in range(60):
            hr = "{}:{}".format(str(i).zfill(2), str(j).zfill(2))
            print(hr, getTimeInText(hr))
