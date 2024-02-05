import sys
input = sys.stdin.readline

n,x = map(int,input().split())
arr = list(map(int,input().split()))

result = sum(arr[0:x])
cnt = 1
value = result

for i in range(x,n):
    value -= arr[i-x]
    value += arr[i]
    if value>result:
        result = value
        cnt = 1
    elif value == result:
        cnt+=1
    
if result == 0:
    print("SAD")
else:
    print(result)
    print(cnt)