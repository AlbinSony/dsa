from typing import *

def getSingleElement(arr : List[int]) -> int:
    # Write your code here.
    maxi=max(arr)
    n=len(arr)
    hash = [0] * (maxi + 1)
    for i in range(n):
        hash[arr[i]]+=1
    for i in range(n):
        if hash[arr[i]]==1:
            return arr[i]
    
