import sys
input = sys.stdin.readline

n,k = map(int,input().split())
arr = list(map(int,input().rstrip().split()))

result_arr = []
for i in range(len(arr)-1):
    result_arr.append(arr[i+1]-arr[i])
result_arr.sort(reverse = True)

print(sum(result_arr[k-1:]))