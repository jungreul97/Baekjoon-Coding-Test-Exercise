import sys
input = sys.stdin.readline

n,k = map(int,input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))
arr.sort(key = lambda x : (x[1],x[2],x[3]), reverse = True)

result = 0
for i in range(n):
    if arr[i][0] == k:
        cnt = i
        for j in range(i-1,-1,-1):
            if arr[i][1:] == arr[j][1:]:
                cnt-=1
            else:
                break
        if cnt == 0:
            result = 1
        else:
            result = cnt+1
        break
print(result)