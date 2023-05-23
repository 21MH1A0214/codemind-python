n = int(input())
l = list(map(int,input().split()))
sl,zl = [],[]
for i in l:
    if i!=0:
        sl.append(i)
    else:
        zl.append(i)
print(*(sl+zl))