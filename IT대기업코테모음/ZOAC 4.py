import sys
input = sys.stdin.readline

h,w,n,m = map(int,input().split())
x,y = 0,0
if h%(n+1) == 0:
    x = h//(n+1)
else:
    x = h//(n+1) +1

if w%(m+1) == 0:
    y = w//(m+1)
else:
    y = w//(m+1) +1


print(x*y)