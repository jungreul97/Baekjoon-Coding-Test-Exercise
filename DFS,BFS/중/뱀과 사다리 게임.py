import sys
from collections import deque

def bfs(v):
    queue = deque()
    queue.append(v)
    while queue:
        v = queue.popleft()
        for i in sadari:
            if i[0] == v:
                if visited[i[1]]>visited[v] or visited[i[1]] == 0:
                    visited[i[1]] = visited[v]
                v = i[1]
        for j in bam:
            if j[0] == v:
                if visited[j[1]]>visited[v] or visited[j[1]] == 0:
                    visited[j[1]] = visited[v]
                v = j[1]
        for i in range(1,7):
            if v+i>100:
                continue
            elif visited[v+i] == 0 or visited[v+i]>visited[v]+1:
                visited[v+i] = visited[v]+1
                queue.append(v+i)
                
n,m = map(int,sys.stdin.readline().split())

arr=[i for i in range(0,101)]

sadari = []
bam = []
for i in range(n):
    sadari.append(list(map(int,input().split())))
for i in range(m):
    bam.append(list(map(int,input().split())))

visited = [0]*(101)
bfs(1)
# print(visited)
print(visited[100])