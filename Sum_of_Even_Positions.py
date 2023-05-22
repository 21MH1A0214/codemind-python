n = int(input())
l = list(map(int,input().split()))
es = 0
for i in range(0,len(l)):
    if(i%2==0):
        es = es+l[i]
print(es)