def funny(s):
    return " ".join([i[::-1].capitalize() for i in s.split()])
