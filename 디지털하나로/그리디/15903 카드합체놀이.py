import sys,heapq
input = sys.stdin.readline

n,m = map(int,input().split())
arr = list(map(int,input().split()))

q = []
for i in range(n):
    heapq.heappush(q,arr[i])

while m>0:
    a = heapq.heappop(q)
    b = heapq.heappop(q)
    
    heapq.heappush(q,a+b)
    heapq.heappush(q,a+b)
    m-=1
print(sum(q))