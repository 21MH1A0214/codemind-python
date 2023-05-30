n=input().lower()
temp=[]
for i in n:
    if n.count(i)==1 and  i!=" ":
        temp.append(i)
        temp.sort()
print(len(temp))