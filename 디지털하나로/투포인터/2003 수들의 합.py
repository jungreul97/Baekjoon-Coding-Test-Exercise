import sys
input = sys.stdin.readline

N,M = map(int,input().split())
arr = list(map(int,input().split()))
cnt = 0
start,end = 0,1
while start <= end :
    # print(start,end)
    # print(*arr[start : end ])
    if sum(arr[start:end]) == M : 
        cnt+=1
        start += 1
        end += 1
    elif sum(arr[start:end]) > M :
        start += 1
    else:
        end += 1
    if end == N+1: 
        start+=1
        end-=1
print(cnt)
