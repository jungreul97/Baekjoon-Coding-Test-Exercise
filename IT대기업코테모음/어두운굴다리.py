import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
arr = list(map(int,input().split()))

result = max(arr[0],n-arr[-1])
for i in range(1,len(arr)-1):
    max_light = 0
    tmp = arr[i+1]-arr[i]
    if tmp%2 == 0:
        max_light = tmp//2
    else:
        max_light = (tmp//2)+1
    result = max(result,max_light)

print(result)

