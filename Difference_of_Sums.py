n = int(input())
c,e = 0,0
for i in range(1,n+1):
    d = i*i
    c+=d
    e+=i
print(abs((e**2)-c))