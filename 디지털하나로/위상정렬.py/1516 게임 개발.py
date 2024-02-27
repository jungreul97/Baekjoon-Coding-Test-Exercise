import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
inDegree = [0]*(n+1)
time = [0] * (n+1)
answer = [0] * (n+1)

for i in range(1,n+1):
    cmd = list(map(int,input().split()))
    time[i] = cmd[0]
    for j in range(1,len(cmd)-1):
        inDegree[i] += 1
        graph[cmd[j]].append(i)
# print(graph)
# print("time>>>>>>>>>>", time)
# print(inDegree)

queue = deque()
for i in range(1,n+1):
    if inDegree[i] == 0:
        queue.append(i)

while queue:
    now = queue.popleft()
    answer[now] += time[now]
    # print(now,graph[now])
    for i in graph[now]:
        inDegree[i] -= 1
        answer[i] = max(answer[i],answer[now]) # 먼저 지어야 하는 선수 건물 짓는데 걸리는 시간으로 갱신
        if inDegree[i] == 0:
            queue.append(i)
        # print(answer)
for i in range(1,n+1):
    print(answer[i])
