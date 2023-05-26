n = int(input())
l = list(map(int,input().split()))
c = 0
for i in l:
    c+=i
a = c//n
if a in l:
    print(True)
else:
    print(False)