a,b,c = map(int,input().split())
if (a>b and a>c):
 l = a
elif (b>a and b>c):
 l = b
elif (c>a and c>b):
 l = c
 print(l)
