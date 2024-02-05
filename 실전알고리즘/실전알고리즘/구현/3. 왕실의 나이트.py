import sys
input = sys.stdin.readline

result = 0
x,y = map(int,input().split())
dx = [-2,-2,2,2,-1,-1,1,1]
dy  = [-1,1,-1,1,-2,2,-2,2]

for i in range(8):
    nx = x+dx[i]
    ny = y+dy[i]
    if 0<=nx<8 and 0<=ny<8:
        result+=1
print(result)