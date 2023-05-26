n = int(input())
for i in range(n):
    m = int(input())
    s = str(m)
    x = s[::-1]
    y = int(x)
    if m==y:
        print(True)
    else:
        print(False)