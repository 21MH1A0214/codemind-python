def sqrSum(n):
    tot = 0
    while n>0:
        tot+=pow(n%10,2)
        n//=10
    return tot
num = int(input())
temp = num
while temp!=1 and temp!=4:
    temp = sqrSum(temp)
if temp==1:
    print(True)
else:
    print(False)