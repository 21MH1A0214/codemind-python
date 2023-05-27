s = input()
c = 0
le= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in s:
    if i in le:
        c+=1
print(c)