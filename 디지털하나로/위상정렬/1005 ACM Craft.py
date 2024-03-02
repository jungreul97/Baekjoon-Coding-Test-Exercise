import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

while T>0:
    N,K = map(int,input().split())
    cost = [0] + list(map(int,input().split()))
    graph = [[] for i in range(N+1)]
    inDegree = [0]*(N+1)
    for _ in range(K):
        a,b = map(int,input().split())
        graph[a].append(b)
        inDegree[b]+=1
    target = int(input())

    # print("graph>>>>",graph)
    # print("inDegree>>>",inDegree)

    queue = deque()
    total = [0]*(N+1)
    for i in range(1,N+1):
        if inDegree[i] == 0:
            queue.append((i,cost[i]))
            total[i] = cost[i]
    while queue:
        now,cost_now = queue.popleft()
        for j in graph[now]:
            inDegree[j]-=1
            if total[j] != 0:
                total[j] = max(total[j],cost[j]+cost_now)
            else:
                total[j] += cost_now+cost[j]
            if inDegree[j] == 0:
                queue.append((j,total[j]))
        # print("toatl>>>>",total)
    print(total[target])
    T-=1

