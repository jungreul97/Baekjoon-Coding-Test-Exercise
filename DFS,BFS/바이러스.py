import sys
from collections import deque
input = sys.stdin.readline
cpn = int(input())
nn = int(input())

graph = [[]*cpn for i in range(cpn+1)]

for i in range(nn):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (cpn+1)
visited[1] = True

queue = deque()
queue.append(1)
while queue:
    cpun = queue.popleft()
    visited[cpun] = True
    for i in graph[cpun]:
        if not visited[i]:
            visited[cpun] = True
            queue.append(i)

print(visited.count(True)-1)