def nStarDiamond(n: int) -> None:
    # Write your code here.
    for i in range(0,n):
        for j in range(0,n-i-1):
            print(" ",end="")
        for j in range(0,2*i+1):
            print("*",end="")
        for j in range(0,n-i-1):
            print(" ",end="")
        print()
    for i in range(0,n):
        for j in range(0,i):
            print(" ",end="")
        for j in range(0,2*n-(2*i+1)):
            print("*",end="")
        for j in range(0,i+1):
            print(" ",end="")
        print()