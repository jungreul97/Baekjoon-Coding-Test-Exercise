import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
m = int(input())
result = 0
if sum(arr)<=m:
    print(max(arr))
else:
    start = 0
    end = max(arr)

    while start<=end:
        mid = (start+end)//2
        sum = 0
        for i in arr:
            if i<mid:
                sum+=i
            else:
                sum+=mid
        if sum == m:
            result = mid
            break
        elif sum<m:
            result = mid
            start = mid+1
        elif sum>m:
            end = mid-1
        # print('mid',mid,'sum',sum)
    print(result)