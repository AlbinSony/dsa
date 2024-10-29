def printSum(i):
    if i==0:
        return 0
    return i + printSum(i-1)
n=int(input("enter number: "))
print(printSum(n))