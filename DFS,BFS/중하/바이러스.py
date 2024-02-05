import sys
from collections import deque
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

arr = [[] for _ in range(n+1)]
arr[0] = [0,0]
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)

# print(arr)
visited = [False] * (n+1)

def bfs(v):
    queue = deque()
    queue.append(v)
    while queue:
        v = queue.popleft()
        for i in arr[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

bfs(1)
# print(visited)
print(visited.count(True)-1)