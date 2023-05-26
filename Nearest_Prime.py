import math
def isprime(n):
    sq = int(math.sqrt(n))
    for i in range(2,sq+1):
        if n%i==0:
            return False
    return True
p = int(input())
for i in range(p):
    n = int(input())
    if isprime(n):
        print(n)
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
        if c<d:
            print(m)
        elif c>d:
            print(p)
        else:
            print(p)