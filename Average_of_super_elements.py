n = int(input())
d = list(map(int,input().split()))
a = []
for i in d:
    if d.count(i)==i and i not in a:
        a.append(i)
if len(a)==0:
    print(-1)
else:
    print("{:.2f}".format(sum(a)/len(a)))