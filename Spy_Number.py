n = int(input())
r = str(n)
s,p = 0,1
for i in r:
    j = int(i)
    s+=j
    p*=j
if p==s:
    print("Spy Number")
else:
    print("Not Spy Number")