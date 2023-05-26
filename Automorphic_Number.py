n = int(input())
q = len(str(n))
s = n**2
l = s%pow(10,q)
if l==n:
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')