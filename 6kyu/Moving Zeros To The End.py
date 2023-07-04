# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

# Example

# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

# My solution

def move_zeros(lst):
    zero = lst.count(0)
    lst = [x for x in lst if x != 0]
    for i in range(zero):
        lst.append(0)
    return lst