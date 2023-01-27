# You get an array of numbers, return the sum of all of the positives ones.

# Example [1,-4,7,12] => 1 + 7 + 12 = 20

# Note: if there is nothing to sum, the sum is default to 0.

# MySolution
def positive_sum(arr):
    total = 0
    for i in arr:
        if i < 0:
            continue
        else:
            total = total + i
    return total