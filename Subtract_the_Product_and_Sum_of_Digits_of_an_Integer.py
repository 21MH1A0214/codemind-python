n = int(input())
m,s=1,0
x = str(n)
for i in x:
    p = int(i)
    m*=p
    s+=p
print(m-s)