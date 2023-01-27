# Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

# You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
# The array will always contain letters in only one case.

# Example:

# ['a','b','c','d','f'] -> 'e'
# ['O','Q','R','S'] -> 'P'
# (Use the English alphabet with 26 letters!)

# MySolution
def find_missing_letter(chars):
    alp = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    whr = alp.find(chars[0])
    tot = alp[whr: whr+len(chars)+1]
    
    for e,i in enumerate(tot):
        if chars[e] != tot[e]:
            return tot[e]