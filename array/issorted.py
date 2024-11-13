def isSorted(n: int,  a: [int]) -> int:
    # Write your code here.
    for i in range(0,n):
        if a[i]<a[i-1]:
            return 1
        else:
            return 0
    pass
