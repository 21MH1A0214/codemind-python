k=input().split()
a=0
b=0
for i in k:
    n=[]
    for j in i:
        n.append(ord(j))
    a=a+min(n)
    b=b+max(n)
print(abs(a-b))