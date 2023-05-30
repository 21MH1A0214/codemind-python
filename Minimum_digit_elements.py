n = int(input())
l = list(map(int,input().split()))
c = 0
m = min(l)
o = str(m)
p = len(o)
for i in l:
    k = str(i)
    if p==len(k):
        c+=1
print(c)