from typing import *

def missingNumber(a : List[int], N : int) -> int:
    # Write your code here.
    ssum=(N*(N+1))//2
    ss=0
    for i in a:
        ss+=i
    return ssum-ss




