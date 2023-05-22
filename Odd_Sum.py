n = int(input())
l = list(map(int,input().split()))
os = 0
for i in l:
    if(i%2!=0):
        os = os+i
print(os)