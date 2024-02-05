import sys
from collections import deque

def bfs(x,y):
    global result 
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    while queue:
        # print(queue)
        x,y = queue.popleft()
        result+=1
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            else:
                if not visited[nx][ny] and arr[nx][ny] == 1:
                    queue.append((nx,ny))
                    visited[nx][ny] = True
                    
n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(list(map(int,input())))

visited = [[False]*n for j in range(n)]
result = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

result_arr=[]

for i in range(n):
    for j in range(n):
        if not visited[i][j] and arr[i][j] == 1:
            result = 0
            bfs(i,j)
            result_arr.append(result)
# print(arr)
# print(visited)

print(len(result_arr))

result_arr.sort()
# print(result_arr)
for i in result_arr:
    print(i)
    


