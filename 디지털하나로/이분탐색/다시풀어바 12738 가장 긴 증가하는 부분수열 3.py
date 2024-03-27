import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))

result= [arr[0]]
for num in arr[1:]:
    if num > result[-1]: result.append(num)
    else:
        start,end = 0,len(result)
        idx = 0
        while start<=end:
            mid = (start+end)//2
            if result[mid] == num : 
                idx = mid
                break
            elif result[mid]<num:
                idx = mid
                start = mid+1
            else:
                idx = mid
                end = mid-1
        result[idx] = num
    print(result)

# print(result)
print(len(result))


    