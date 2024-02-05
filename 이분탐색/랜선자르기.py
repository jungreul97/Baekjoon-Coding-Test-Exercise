import sys
input = sys.stdin.readline

k,n = map(int,input().split())
arr = []
for _ in range(k):
    arr.append(int(input()))

start = 1
end = max(arr)
count = 0
answer = 0

while start<=end:
    count = 0
    mid = (start+end)//2
    for i in arr:
        count+=(i//mid)
    # print('count',count)
    if count>=n:
        start = mid+1
        answer = mid
    else:
        end = mid-1


print(answer)
    
