# import sys
# import heapq
# input = sys.stdin.readline
# INF = int(1e9)

# n,d = map(int,input().split())
# graph = [[] for i in range(d+1)]
# for i in range(d):
#     graph[i].append((i+1,1))
# distance = [INF] * (d+1)

# for _ in range(n):
#     a,b,c = map(int,input().split())
#     if b>d:continue
#     graph[a].append((b,c))

# def dijkstra():
#     q = []
#     heapq.heappush(q,(0,0))
#     while q:
#         d,now = heapq.heappop(q)
#         #무한대가 아니고 처리된적 있으면 넘김
#         if distance[now]<d:continue

#         for i in graph[now]:
#             cost = i[1]+d

#             if distance[i[0]]>cost:
#                 distance[i[0]] = cost
#                 heapq.heappush(q,(cost,i[0]))

# dijkstra()
# print(distance[d])

import sys
import heapq
input = sys.stdin.readline

n,d = map(int,input().split())
INF = int(1e9)
distance = [INF] * (d+1)

graph = [[] for _ in range(d+1)]
for i in range(d):
    graph[i].append((i+1,1))


for _ in range(n):
    a,b,c = map(int,input().split())
    if b>d:
        continue
    graph[a].append((b,c))

q = []
heapq.heappush(q,(0,0))
while q:
    dist,now = heapq.heappop(q)
    if distance[now]<dist:
        continue

    for i in graph[now]:
        cost = dist+i[1]
        if cost<distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q,(cost,i[0]))

print(distance[d])













