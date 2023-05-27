s = input()
c = 0
l = 'abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in s:
    if i not in l:
        c+=1
print(c)