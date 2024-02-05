import sys
#최대 n의 크기가 크지 않으면 플로이드 워셜 알고리즘 사용하기
n,m = map(int,sys.stdin.readline().split())
INF = int(1e9)
arr = [[INF]*(n+1) for _ in range(n+1)]

for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    arr[a][b] = 1
    arr[b][a] = 1

x,k = map(int,sys.stdin.readline().split()) 

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            arr[a][b] = min(arr[a][b],arr[a][k]+arr[k][b])

distance = arr[1][k]+arr[k][x]

if distance>=INF:
    print(-1)
else:
    print(distance)
 