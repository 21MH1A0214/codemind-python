s = input().split()
v = 'aeiouAEIOU'
l = []
for i in s:
    c = 0
    for j in i:
        if j in v:
            c+=1
    l.append(c)
print(*l)
    