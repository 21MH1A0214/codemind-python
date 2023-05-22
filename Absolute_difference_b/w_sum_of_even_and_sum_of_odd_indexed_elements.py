n = int(input())
l = list(map(int,input().split()))
es,os = 0,0
for i in range(0,len(l)):
    if(i%2==0):
        es = es+l[i]
    else:
        os = os+l[i]
print(abs(es-os))