n,m = map(int,input().split())
num = list(map(int,input().split()))

arr = [False]*(n+1)

result = 0
for i in num:
    for j in range(1,n+1):
        if arr[j]:
            continue
        else:
            if j%i == 0:
                arr[j] = True

for i in range(1,n+1):
    if arr[i]:
        result+=i

print(result)