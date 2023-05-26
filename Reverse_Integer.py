n=int(input())
f=0
rev=0
if n<0:
    f=1
    n=-n
if n>0:
    while(n>0):
        r=n%10
        rev=rev*10+r
        n=n//10
if f:
    print(-rev)
else:
    print(rev)