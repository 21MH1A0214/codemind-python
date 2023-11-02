s = input()
n = '1234567890'
l = []
for i in s:
    if i in n:
        l.append(i)
count=0
for j in l:
    count+=int(j)
print(count)