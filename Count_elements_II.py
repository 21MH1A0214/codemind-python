m,n = map(int,input().split())
l = list(map(int,input().split()))
l1 = list(map(int,input().split()))
a,b = set(l),set(l1)
c,s,k = 0,0,0
for i in a:
    if i not in b:
        s+=1
for j in b:
    if j not in a:
        k+=1
c = s+k
print(c)