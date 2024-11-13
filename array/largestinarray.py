from sys import *
from collections import *
from math import *

def largestElement(arr: [], n: int) -> int:
    max_element = arr[0]
    
    for num in arr:
        if max_element<num:
            max_element = num
    
    return max_element
