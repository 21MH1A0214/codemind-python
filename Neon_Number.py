n = int(input())
sq = n*n
sum = 0
while sq>0:
    sum+=sq%10
    sq//=10
if n==sum:
    print('Neon Number')
else:
    print('Not Neon Number')