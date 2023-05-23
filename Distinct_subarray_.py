l = int(input())
r = int(input())
c = 0
for i in range(l,r+1):
    if i%2!=0:
        c+=1
        for j in range(i,r+1):
            d = i+j
            if d%2==0:
                continue
            else:
                c+=1
    else:
        for j in range(i,r+1):
            d = i+j
            if d%2==0:
                continue
            else:
                c+=1
print(c)