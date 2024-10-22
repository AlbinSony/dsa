def checkArmstrong(n):
    sum=0
    dummy=n
    while(n>0):
        ld=n%10
        sum=sum+(ld*ld*ld)
        n=n//10
    if(sum==dummy):
        return True
    else:
        return False
n = int(input()) 
if checkArmstrong(n):
    print("true")
else:
    print("false")

    