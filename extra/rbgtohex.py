#Author: ahmelq -  github.com/ahmedelq/
#License: MIT
#This is a solution of the challange: https://old.reddit.com/r/dailyprogrammer/comments/a0lhxx/20181126_challenge_369_easy_hex_colors/

def rbgToHex(*clr):
    """Given a color in rbg, convert it to hexadecimal color""" 
    if len(clr) != 3 or max(clr) > 255 or min(clr) < 0: raise ValueError('invalid color')
    return '#' + ''.join([
        hex(c)[2:].zfill(2) for c in clr 
        ]).upper()
def blend(clrs):
    """Given a list of hexcolor, will return their average"""
    import re
    clrs_count = len(clrs)
    rbg = [list(
            map(lambda hex_val: int(hex_val, 16),
            re.match(r"#(\w{2})(\w{2})(\w{2})", clr).groups()))
            for clr in clrs ]
    result = list(map(lambda x: x // clrs_count, map(sum, zip(*rbg))))
    print(result)
    return rbgToHex(*result) 
    
if __name__ == "__main__":
    print(
        rbgToHex(255, 255, 255), 
        rbgToHex(255, 99, 71), 
        rbgToHex(184, 134, 11),
        rbgToHex(189, 183, 107),
        rbgToHex(0, 0, 205),
        blend(["#E6E6FA", "#FF69B4", "#B0C4DE"]),
        blend(["#000000", "#778899"])
        )
 

    