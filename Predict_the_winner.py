n = int(input())
l = list(map(int,input().split()))
e,o = [],[]
s1,s2 = 0,0
if n%2==0:
    e = l[:n//2]
    o = l[n//2:]
else:
    e = l[:(n//2)+1]
    o = l[(n//2)+1:]
for i in e:
    s1= s1+i
for j in o:
    s2 = s2+j
s3 = abs(s1-s2)
if s3%4==0:
    print('X')
else:
    print('Y')