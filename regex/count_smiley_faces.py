
#Author: ahmelq -  github.com/ahmedelq/
#License: MIT
#This is a solution of https://www.codewars.com/kata/583203e6eb35d7980400002a


def countSmileys(arr):
    import re
    return len(
        re.compile(r'[:;][-~]?[\)D]')
        .findall(' '.join(arr))
        )


if __name__ == "__main__":
    print(
        countSmileys([':)', ';(', ';}', ':-D']),        # should return 2
        countSmileys([';D', ':-(', ':-)', ';~)']),      # should return 3
        countSmileys([';]', ':[', ';*', ':$', ';-D'])   # should return 1
        )