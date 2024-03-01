import sys
import heapq
input = sys.stdin.readline

n,m,k,x = map(int,input().split())
graph = [[] for _ in range(n+1)]
distance = [int(1e9)] * (n+1)

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
q = []
heapq.heappush(q,(0,x))
distance[x] = 0

# print(graph)
while q:
    dist, now = heapq.heappop(q)
    if distance[now]<dist : continue
    for j in graph[now]: 
        cost = dist+1
        if cost< distance[j]:
            distance[j] = cost
            heapq.heappush(q,(dist+1,j))
# print(distance)
if k in distance:
    for i in range(1,n+1):
        if distance[i] == k:
            print(i)
else:
    print(-1)




