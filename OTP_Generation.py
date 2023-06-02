n = int(input())
s = str(n)
l = list(s)
k = []
for i in l:
    j = int(i)
    if j%2!=0:
        k.append(j*j)
for m in k:
    print(m,end='')