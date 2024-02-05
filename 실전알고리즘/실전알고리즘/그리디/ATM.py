n = int(input())

arr = sorted(list(map(int,input().split())))
result = 0
for i in range(1,n):
    arr[i] = arr[i-1]+arr[i]

print(sum(arr))