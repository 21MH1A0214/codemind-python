n = int(input())
a = list(map(int,input().split()))
l,k = [],[]
c,s = 0,0
e,f = map(int,input().split())
for i in range(e,f+1):
    l.append(i)
for i in a:
    if i not in l:
        k.append(i)
        c+=1
print(sum(k))