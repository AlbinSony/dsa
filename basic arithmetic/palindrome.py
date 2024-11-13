def is_palindrome(n):
    dummy = n
    revNum = 0   
    while n > 0:
        ld = n % 10  
        revNum = (revNum * 10) + ld 
        n = n // 10 
    if revNum == dummy:
        return True
    else:
        return False
        
n = int(input()) 
print(is_palindrome(n))
