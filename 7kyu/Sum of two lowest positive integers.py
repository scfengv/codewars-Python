# Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.

# For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

# [10, 343445353, 3453445, 3453545353453] should return 3453455.

# MySolution
def sum_two_smallest_numbers(numbers):
    min1 = None
    min2 = None
    
    for i in numbers:
        if min1 == None or i < min1:
            min1 = i
            
    numbers.remove(min1)
    
    for j in numbers:
        if min2 == None or j < min2:
            min2 = j
            
    total = min1 + min2
    
    return total