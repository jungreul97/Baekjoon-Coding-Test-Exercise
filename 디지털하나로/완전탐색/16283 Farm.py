import sys
input = sys.stdin.readline

a,b,n,w = map(int,input().split())
x,y = 0,0
result = 0
for i in range(1,n):
    if i*a + (n-i)*b == w:
        x,y = i,n-i
        result +=1
    if result == 2:
        break
if (x == 0 and y == 0) or result == 2:
    print(-1)
else:
    print(x, y)