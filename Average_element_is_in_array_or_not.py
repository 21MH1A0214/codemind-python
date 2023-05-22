n = int(input())
l = list(map(int,input().split()))
s = 0
for i in l:
    s = s+i
    avg = s//n
if avg in l:
    print(True)
else:
    print(False)