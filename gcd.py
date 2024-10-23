# n1=int(input())
# n2=int(input())
# gcd=0
# for i in range(1,n1):
#     if n1%i==0 and n2%i==0:
#         gcd=i
# print(gcd)   

#optimal
n1 = int(input())
n2 = int(input())
gcd = 1 
for i in range(min(n1, n2), 0, -1): 
    if n1 % i == 0 and n2 % i == 0:
        gcd = i
        break
print(gcd)
