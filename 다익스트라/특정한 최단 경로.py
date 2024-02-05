import sys
input = sys.stdin.readline
import heapq

n,m = map(int,input().split())
arr = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    arr[a].append((b,c))
    arr[b].append((a,c))
first,second = map(int,input().split())
print(arr)
INF = int(1e9)
distance = [INF,False]*(n+1)
distance[1] = 0

q = []
check = False
heapq.heappush(q,(0,1,check))
while q:
    dist,now,visit = heapq.heappop(q)


