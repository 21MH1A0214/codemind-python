n = int(input())
l = list(map(int,input().split()))
for i in range(0,n):
    for j in range(0,n):
        if i!=j:
            if l[i]==l[j]:
                l[j]= -1
for j in l:
    if j>-1:
        print(j,end = ' ')