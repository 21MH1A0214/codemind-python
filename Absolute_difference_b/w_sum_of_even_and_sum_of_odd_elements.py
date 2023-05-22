n = int(input())
l = list(map(int,input().split()))
es,os = 0,0
for i in l:
    if(i%2==0):
        es = es+i
    else:
        os = os+i
print(abs(es-os))