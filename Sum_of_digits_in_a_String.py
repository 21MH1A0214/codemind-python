s = str(input())
n = '1234567890'
l = []
c= 0
for i in s:
    if i in n:
        l.append(i)
for j in l:
    c+=int(j)
print(c)