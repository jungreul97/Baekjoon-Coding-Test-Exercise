import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for i in range(n+1)]
distance = [int(1e9)]*(n+1)

for _ in range(m):
    start,end,cost = map(int,input().split())
    graph[start].append((end,cost))

start_node,end_node = map(int,input().split())
distance[start_node] = 0
mid_node = [0]*(n+1)
q = []
# print(graph)
heapq.heappush(q,(0,start_node))
while q:
    # print("queue>>>>>",q)
    dist,now = heapq.heappop(q)
    # print(dist,now)
    if distance[now] < dist : 
        continue
    for i in graph[now]:
        cost = dist+i[1]
        if cost<distance[i[0]]: # 더짧을때만 들어갔네...
            mid_node[i[0]] = now # 노드에서 가장 가까운게 현재 노드이므로 기록
            distance[i[0]] = cost
            heapq.heappush(q,(cost,i[0]))
            # print(i,mid_node)
            # print(distance)
print(distance[end_node])
# print(distance)
# print(mid_node)

path = [end_node]
now = end_node
while now != start_node:
    # print(now)
    now =  mid_node[now]
    path.append(now)

path.reverse()

print(len(path))
print(' '.join(map(str, path)))


# 5
# 8
# 1 2 2
# 1 3 3
# 1 4 1
# 1 5 10
# 2 4 2
# 3 4 1
# 3 5 1
# 4 5 3
# 1 5

# 4
# 3
# 1 3 5