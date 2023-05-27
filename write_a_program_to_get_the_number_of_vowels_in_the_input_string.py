s = input()
v = 'aeiouAEIOU'
l = []
for i in s:
    if i in v:
        l.append(i)
print(len(l))