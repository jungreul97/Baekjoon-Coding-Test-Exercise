import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(str,input().rstrip())))
sx,sy = 0,0
print(graph)
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'S':
            sx,sy = i,j
            break
    if 'S' in graph[i]:
        break
visited = [[False]*m for _ in range(n)]
result = 'KAKUS'
