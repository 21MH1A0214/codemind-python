n = int(input())
c = 0
s = str(n)
for i in range(len(s)):
    if s[i]==0:
        print('Invalid')
    else:
        c+=1
if c==10:
    print('Valid')
else:
    print('Invalid')