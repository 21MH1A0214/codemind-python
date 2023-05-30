m,n = map(int,input().split())
l = list(map(int,input().split()))
l1 = list(map(int,input().split()))
l2 = []
for i in l:
    if i not in l1 and i not in l2:
        l2.append(i)
for j in l1:
    if j not in l and j not in l2:
        l2.append(j)
print(*l2)