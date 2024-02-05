import sys
input = sys.stdin.readline
from collections import deque

n,m,k = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input().rstrip())))

visited = [[[0]*(k+1) for _ in range(m)] for _ in range(n)]
visited[0][0][k] = 1
dx = [-1,1,0,0]
dy = [0,0,-1,1]
print(graph)
def bfs():
    queue = deque()
    queue.append((0,0,k))
    while queue:
        x,y,b = queue.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y][b]
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=y<m:
                if graph[nx][ny] == 1 and b>0 and visited[nx][ny][b-1] == 0:
                    visited[nx][ny][b-1] = visited[x][y][b]+1
                    queue.append((nx,ny,b-1))
                elif graph[nx][ny] == 0 and visited[nx][ny][b] == 0:
                    visited[nx][ny][b] = visited[x][y][b]+1
                    queue.append((nx,ny,b))
    return -1
print(visited)
print(bfs())