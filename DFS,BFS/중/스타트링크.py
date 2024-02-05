import sys
from collections import deque

def bfs(v):
    queue = deque()
    queue.append(v)
    while queue:
        # print(queue)
        v = queue.popleft()
        if v+u!=s and v+u<=f and visited[v+u] == 0 :
            visited[v+u] = visited[v]+1
            queue.append(v+u)
        if v-d!=s and v-d>0 and visited[v-d] == 0 :
            visited[v-d] = visited[v]+1
            queue.append(v-d)

f,s,g,u,d = map(int,sys.stdin.readline().split())

visited = [0]*(f+1)
bfs(s)
# print(visited)

if visited[g] == 0 and s!=g:
    print('use the stairs')
else:
    print(visited[g])