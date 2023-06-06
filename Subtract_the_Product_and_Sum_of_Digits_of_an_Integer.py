n = int(input())
m,sp = 1,0
s = str(n)
for i in s:
    m = m*int(i)
    sp = sp+int(i)
print(abs(m-sp))