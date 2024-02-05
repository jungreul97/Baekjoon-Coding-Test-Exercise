import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
answer = 0

graph = []
for _ in range(n):
    graph.append(list(map(int,input().strip())))


visited = [[False]*m for _ in range(n)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

for i in range(n):
    for j in range(m):
        print(visited[i][j],graph[i][j])
        if not visited[i][j] and graph[i][j] == 0:
            print(i,j)
            answer+=1
            visited[i][j] = True
            queue = deque()
            queue.append((i,j))
            while queue:
                x,y = queue.popleft()
                print(x,y)
                for v in range(4):
                    nx = x+dx[v]
                    ny = y+dy[v]

                    if nx<0 or nx>=n or ny<0 or ny>=m:
                        continue
                    if not visited[nx][ny] and graph[nx][ny] == 0:
                        print(nx,ny)
                        visited[nx][ny] = True
                        queue.append((nx,ny))

print(answer)
                
