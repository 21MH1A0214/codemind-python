import math
def isprime(n):
    sq = int(math.sqrt(n))
    for i in range(2,sq+1):
        if n%i==0:
            return False
    return True
n = int(input())
r = isprime(n)
if r==True:
    print('prime')
else:
    print('not a prime')