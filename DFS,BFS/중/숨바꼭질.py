import sys
from collections import deque

def bfs(v):
    queue = deque()
    queue.append(v)
    while queue:
        v = queue.popleft()
        if v+1!=n and v+1<=100000 and (visited[v+1] == -1 or visited[v+1]>visited[v]+1):
            visited[v+1] = visited[v]+1
            queue.append(v+1)
        if v-1!=n and v-1>=0 and (visited[v-1] == -1 or visited[v-1]>visited[v]+1):
            visited[v-1] = visited[v]+1
            queue.append(v-1)
        if v*2!=n and v*2<=100000 and (visited[v*2] == -1 or visited[v*2]>visited[v]):
            visited[v*2] = visited[v]
            queue.append(v*2)

n,k = map(int,sys.stdin.readline().split())
visited = [-1]*100001
visited[n] = 0
bfs(n)
print(visited[k])