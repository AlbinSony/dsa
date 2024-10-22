def countDigits(n: int) -> int:
    count=0
    while n>0:
        ld=n%10
        count+=1
        n=n//10
    return count

