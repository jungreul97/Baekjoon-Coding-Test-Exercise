n = int(input())
arr = [0 for i in range(301)]
for i in range(n):
    arr[i] = int(input())

result = [0 for i in range(301)]

result[0] = arr[0]
result[1] = arr[0]+arr[1]
result[2] = max(arr[1]+arr[2],arr[0]+arr[2])
for i in range(3,n):
    result[i] = max(result[i-3]+arr[i-1]+arr[i],result[i-2]+arr[i])



print(result[n-1])





