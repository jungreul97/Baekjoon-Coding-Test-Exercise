import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())

arr = []

for _ in range(n):
    arr.append(list(map(int,input().strip().split())))

answer = 0
result = 0

visited = [[False]*(m) for j in range(n)]

dx = [1,-1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    cnt = 1
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx>=n or nx<0 or ny>=m or ny<0:
                continue
            if not visited[nx][ny] and arr[nx][ny] == 1:
                visited[nx][ny] = True
                cnt+=1
                queue.append((nx,ny))
    return cnt

for i in range(n):
    for j in range(m):
        if not visited[i][j] and arr[i][j] == 1:
            dfsresult = dfs(i,j)
            answer+=1
            result = max(result,dfsresult)

print(answer)
print(result)


