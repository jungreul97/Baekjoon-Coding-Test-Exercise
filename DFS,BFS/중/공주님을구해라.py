import sys
from collections import deque
answer = float('inf')
def bfs(x,y):
    global sword_time
    global answer
    global gram
    queue = deque()
    queue.append([x,y])
    while queue:
        x,y= queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<=0 or nx>n or ny<=0 or ny>m:
                continue
            else:
                if nx == gx and ny == gy:
                        arr[nx][ny] = arr[x][y]+1
                        gram = True
                        answer = min(arr[nx][ny],answer)
                elif arr[nx][ny] == 0 or arr[nx][ny]>arr[x][y]+1:
                    
                        arr[nx][ny] = arr[x][y]+1
                        queue.append([nx,ny])

n,m,t = map(int,sys.stdin.readline().split())
arr = [[0]*(m+1)]
for i in range(n):
    arr.append([0]+list(map(int,input().split())))
gx = 0
gy = 0
for i in range(n+1):
    for j in range(m+1):
        if arr[i][j] == 2:
            gx = i
            gy = j

sword_time = abs(n-gx)+abs(m-gy)

# print(sword_time)
# print(input_arr)
#print(arr)
# visited = [[False]*(m+1) for j in range(n+1)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

gram = False

bfs(1,1)
# print(arr)
answer+=sword_time
# print(answer)
# print(sword_time)
if arr[n][m]!=0 and answer>arr[n][m]:
    answer = arr[n][m]

if t<answer:
    print("Fail")
elif not gram and arr[n][m] == 0:
    print("Fail") 
else:
    print(answer)

    