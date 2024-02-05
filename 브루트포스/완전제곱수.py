m = int(input())
n = int(input())

arr = [False] * 10001

for i in range(1,10001):
    if i*i<10001:
        arr[i*i] = True

result = 0
min = 10000

for i in range(m,n+1):
    if arr[i]:
        if i<min:
            min = i
        result+=i
if result == 0:
    print(-1)
else:
    print(result)
    print(min)
