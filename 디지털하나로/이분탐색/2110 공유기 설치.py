import sys
input = sys.stdin.readline

N,C = map(int,input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort()
start,end = 1,arr[-1]-arr[0] # 공유기 거리 최소 최대

while start<=end:
    mid = (start+end)//2
    cnt = 1
    pre = arr[0] # 첫번째집에는 공유기 무조건 설치함
    for i in range(1,N):
        if arr[i] >= pre + mid:
            cnt += 1
            pre = arr[i]
    if cnt >= C :
        answer = mid
        start = mid + 1
    else:
        end = mid-1
print(answer)

