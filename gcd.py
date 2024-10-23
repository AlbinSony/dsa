#brute force 1
n1=int(input())
n2=int(input())
gcd=0
for i in range(1,n1):
    if n1%i==0 and n2%i==0:
        gcd=i
print(gcd)   

#brute force 2
n1 = int(input())
n2 = int(input())
gcd = 1 
for i in range(min(n1, n2), 0, -1): 
    if n1 % i == 0 and n2 % i == 0:
        gcd = i
        break
print(gcd)

#optimal

n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))

while n1 > 0 and n2 > 0:
    if n1 > n2:
        n1 = n1 % n2
    else:
        n2 = n2 % n1

if n1 == 0:
    print(n2)
else:
    print(n1)

