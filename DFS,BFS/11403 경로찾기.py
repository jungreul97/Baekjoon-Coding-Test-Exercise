import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[]*n for _ in range(n)]
for i in range(n):
    arr = list(map(int,input().rstrip().split()))
    for j in range(n):
        if arr[j] == 1:
            graph[i].append(j)

result = [[0]*n for _ in range(n)]


for i in range(n):
    for j in graph[i]:
        result[i][j] = 1
        queue = deque()
        queue.append(j)
        while queue:
            node = queue.popleft()
            for k in graph[node]:
                if result[i][k] == 1:
                    continue
                if result[i][k] == 0:
                    result[i][k] = 1
                    queue.append(k)

for i in range(n):
    for j in range(n):
        print(result[i][j],end = ' ')
    print()

        
