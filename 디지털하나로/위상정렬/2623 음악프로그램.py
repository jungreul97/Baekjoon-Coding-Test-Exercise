import sys
from collections import deque
n,m = map(int,input().split())

graph = [[] for i in range(n+1)]
inDegree = [0]*(n+1)

for i in range(m):
    pd = list(map(int,input().split()))
    for j in range(1,pd[0]):
        for k in range(j+1,pd[0]+1):
            if not pd[j] in graph[pd[k]]:
                graph[pd[j]].append(pd[k])
                inDegree[pd[k]]+=1
# print(graph)
# print(inDegree)
queue = deque()
for i in range(1,n+1):
    if inDegree[i] == 0:
        queue.append(i)
answer = []
while queue:
    now = queue.popleft()
    answer.append(now)
    for i in graph[now]:
        inDegree[i]-=1
        if inDegree[i] == 0:
            queue.append(i)

if len(answer) != n or sum(inDegree) != 0:
    print(0)
else:
    for i in answer:
        print(i)