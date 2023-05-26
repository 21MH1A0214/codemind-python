def sq(n):
    t = 0
    while n>0:
        t+=pow(n%10,2)
        n//=10
    return t
num = int(input())
temp = num
while temp!=1and temp!=4:
    temp = sq(temp)
if temp==1:
    print(True)
else:
    print(False)