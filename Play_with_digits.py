def sa(n):
    s=0
    while(n!=0):
        r=n%10
        s+=r
        n=n//10
    return s
n=int(input())
s=list(map(int,input().split()))
c=0
for i in range(n):
    c+=sa(s[i])
print(c)