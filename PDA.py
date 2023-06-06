n = int(input())
l = []
c = 0
for i in range(1,n//2+1):
    if n%i==0:
        l.append(i)
for j in l:
    c+=j
if c==n:
    print("PERFECT")
elif c>n:
    print("ABUNDANT")
else:
    print("DEFICIENT")