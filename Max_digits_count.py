n = int(input())
l = list(map(int,input().split()))
c = 0
m = max(l)
s = str(m)
o = len(s)
for i in l:
    k = str(i)
    if o==len(k):
        c+=1
print(c)