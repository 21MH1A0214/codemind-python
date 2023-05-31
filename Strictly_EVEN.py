n=int(input())
lst=list(map(int,input().split()))
f=0
for i in range(n):
    if i%2==0 and lst[i]%2==1:
        f=1
        break
if(f==0):
    print(True)
else:
    print(False)