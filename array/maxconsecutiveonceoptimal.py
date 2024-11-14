from collections import defaultdict

def get_single_element(arr):
    mpp = defaultdict(int)
    
    # Loop to count the frequency of each element
    for num in arr:
        mpp[num] += 1
    
    # Loop to find the element with a frequency of 1
    for num, count in mpp.items():
        if count == 1:
            return num
    
    return -1  # Return -1 if no element occurs once

# Example usage
arr = [4, 5, 6, 5, 4, 6, 7]  # Example array
print("The single element is:", get_single_element(arr))
