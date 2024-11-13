def printSum(i,sum):
    if i<1:
        print(sum)
        return
    printSum(i-1,sum+i)

n=int(input("enter a number"))
printSum(n,0)