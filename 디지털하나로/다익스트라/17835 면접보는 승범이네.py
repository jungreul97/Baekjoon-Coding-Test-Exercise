import sys,heapq
input = sys.stdin.readline

#도착지점 -> 출발지점 역 다익스트라 진행행 모든 노드에서 도착지로 하면 시간 너무 오래 걸림
N,M,K = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,cost = map(int,input().split())
    graph[b].append((a,cost)) #도착지 -> 출발지 값 저장
targets = list(map(int,input().split()))
result = [float('inf')]*(N+1)

q = []
for i in targets:
    heapq.heappush(q,(0,i))
    result[i] = 0
while q:
    dist,now = heapq.heappop(q)
    if result[now]<dist : continue
    for i in graph[now]:
        cost = dist+i[1]
        if cost<result[i[0]]:
            result[i[0]] = cost
            heapq.heappush(q,(cost,i[0]))

node,max_dist = 0,0
for i in range(1,N+1):
    if result[i] > max_dist and result[i] != float('inf'):
        node = i
        max_dist = result[i]
# print(result)
print(node)
print(max_dist)

