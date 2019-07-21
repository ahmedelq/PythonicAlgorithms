# solution for https://www.codewars.com/kata/strip-comments/train/python

def strip_comments(string, markers):
    res = []
    for s in string.split('\n'):
        indc = list(filter(lambda x: x > -1, [s.find(marker) for marker in markers]))
        if indc:
            s = s[:min(indc)]
            s = s.strip()
        res.append(s)
    return '\n'.join(res)