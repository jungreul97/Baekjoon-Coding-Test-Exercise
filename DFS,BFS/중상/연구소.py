import sys
input = sys.stdin.readline
from collections import deque
import copy

def bfs():
    queue = deque()
    tmp_graph = copy.deepcopy(graph)
    for i in range(n):
        for j in range(m):
            if tmp_graph[i][j] == 2:
                queue.append((i,j))
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if tmp_graph[nx][ny] == 0:
                tmp_graph[nx][ny] = 2
                queue.append((nx,ny))

    global answer
    count = 0
    for i in range(n):
        count+=tmp_graph[i].count(0)
    
    answer = max(answer,count)


def makewall(cnt):
    if cnt == 3:
        bfs()
        return
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                makewall(cnt+1)
                graph[i][j] = 0

n,m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().rstrip().split())))

answer = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

makewall(0)
print(answer)