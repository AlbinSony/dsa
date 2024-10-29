def fact(i):
    if i==0 :
        return 1
    return i*fact(i-1)

n=int(input("enter a num: "))
print(fact(n))


