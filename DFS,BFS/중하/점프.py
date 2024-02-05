import sys
from collections import deque

n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))

visited = [0 for _ in range(n)]

def bfs(v):
    if v == 1:
        return
    queue = deque()
    queue.append(v)
    while queue:
        v = queue.popleft()
        for i in range(1,arr[v]+1):
            if v+i<n and visited[v+i] == 0:
                visited[v+i] = visited[v] + 1
                queue.append(v+i)
bfs(0)
# print(visited)
if visited[n-1] == 0 and n!=1:
    print(-1)
else:
    print(visited[n-1])                

