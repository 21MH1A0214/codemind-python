m,n = map(int,input().split())
l = list(map(int,input().split()))
l1 = list(map(int,input().split()))
l,l1 = set(l),set(l1)
c = 0
for i in l:
    if i in l1:
        c+=1
print(c)