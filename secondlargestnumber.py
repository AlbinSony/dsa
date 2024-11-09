def getSecondOrderElements(n: int,  a: [int]) -> [int]:
    # Write your code here.
    if len(a)<=1:
        return -1
    a.sort()
    return a[-2],a[1]
