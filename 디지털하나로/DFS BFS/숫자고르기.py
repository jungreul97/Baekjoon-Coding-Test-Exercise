import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = []
arr.append([i for i in range(1,n+1)])
tmp = []
for _ in range(n):
    tmp.append(int(input()))
arr.append(tmp)

queue = deque()
visited = [False] * n

for i in range(n):
    if not visited[i]:
        queue.append((arr[i],0,i))
    
    while queue:
        x,idx = queue.popleft()
        if idx == 0:
            


