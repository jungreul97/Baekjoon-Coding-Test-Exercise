import sys
input = sys.stdin.readline

M,N = map(int,input().split())
arr = list(map(int,input().split()))

start,end = 1,max(arr)
answer = 0
while start<=end:
    cnt = 0
    mid = (start+end)//2
    for x in arr:
        if x>= mid:
            cnt += (x//mid)
    if cnt >= M:
        answer = mid
        start = mid+1
    else:
        end = mid-1

print(answer)