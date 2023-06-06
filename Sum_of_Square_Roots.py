m,n = map(int,input().split())
k = []
c = 0
for i in range(m,n+1):
    k.append(i**0.5)
for j in k:
    c+=j
print("{:.2f}".format(c))