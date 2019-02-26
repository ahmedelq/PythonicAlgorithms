def isValidTime(tsmp):
    import re
    return bool(re.match("^([01]?[0-9]|2[0-3]):[0-5][0-9]$", tsmp))

if __name__ == "__main__":
    print("is 13:37 a valid time ? ", isValidTime("13:37"))
    print("is 12:81 a valid time ? ", isValidTime("12:8"))
    print("is 72:45 a valid time ? ", isValidTime("72:45"))
    