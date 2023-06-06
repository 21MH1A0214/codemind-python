def palin(n):
    rev = 0
    t = n
    while n:
        r = n%10
        rev = rev*10+r
        n = n//10
    if t==rev:
        return 1
    else:
        return 0
n = int(input())
f = palin(n)
if f==1:
    print(True)
else:
    print(False)