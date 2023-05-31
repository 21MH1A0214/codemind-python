s = input()
s = s.lower()
l = list(s)
d = []
a = 'abcdefghijklmnopqrstuvwxyz'
for i in l:
    if i in a and i not in d:
        d.append(i)
if len(d)==len(s):
    print(True)
else:
    print(False)