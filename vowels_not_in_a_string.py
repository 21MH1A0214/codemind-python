s = input()
c = 0
v = 'aeiou'
l = []
for i in s:
    if i in v:
        l.append(i)
for j in v:
    if j in l:
        c+=1
        if c==len(v):
            print(0)
    else:
        print(j,end=' ')