# Simple, given a string of words, return the length of the shortest word(s).

# String will never be empty and you do not need to account for different data types.

# MySolution
def find_short(s):
    sh = None
    ss = s.split()
    for i in ss:
        l = len(i)
        if sh == None or l <= sh:
            sh = l
    return sh