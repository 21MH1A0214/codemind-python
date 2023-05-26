def hcf(a,b):
    if b==0:
        return abs(a)
    else:
        return hcf(b,a%b)
m,n = map(int,input().split())
r = hcf(m,n)
print(r)