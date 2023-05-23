n = int(input())
l = list(map(int,input().split()))
l2 = []
l1 = sorted(l)
for i in l1:
    l2.append(i*i)
print(*(sorted(l2)))