import sys
input = sys.stdin.readline

n,answer = map(int,input().split())
arr = list(map(int,input().split()))

start = 0
end = max(arr)
mid = 0
result = 0
while start<=end:
    mid = (start+end)//2
    sum = 0
    for i in arr:
        if i>mid:
            sum+=i-mid

    if sum == answer:
        result = mid
        break

    elif sum>answer:
        result = mid
        start = mid+1

    elif sum<answer:
        end = mid-1

print(result)
            

    
            
