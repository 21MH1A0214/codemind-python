import math
def isprime(n):
    sq = int(math.sqrt(n))
    for i in range(2,sq+1):
        if n%i==0:
            return False
    return True
n = int(input())
if isprime(n):
    print('0')
else:
    m = n+1
    while True:
        if isprime(m):
            
            break
        else:
            m+=1
    p = n-1
    while True:
        if isprime(p):
            
            break
        else:
            p-=1
    c = abs(m-n)
    d = abs(p-n)
    print(min(c,d))