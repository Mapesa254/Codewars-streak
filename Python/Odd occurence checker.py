'''
Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

Examples
[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).
'''


def find_it(seq):
# Initialize an empty dictionary to store counts
    occur = {}  
    
    # Loop through each element in the sequence
    for i in seq:
        if i in occur:
            # Increment the count for the element if it exists in the dictionary
            occur[i] += 1  
        else:
            # Add the element to the dictionary with an initial count of 1 if it's not there
            occur[i] = 1  
    
    # Loop through all items in the dictionary to check for odd counts
    for num, count in occur.items():
        # Check if the count is odd (remainder 1 when divided by 2)
        if count % 2 == 1 :
        # Return the number with an odd count
            return f"The number {num} occurs an odd number of times."  
    
    # If no number with an odd count is found, return None
    return None  
        
print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))  
