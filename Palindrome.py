n = int(input())
s = str(n)
x = s[::-1]
p = int(x)
if p==n:
    print(True)
else:
    print(False)