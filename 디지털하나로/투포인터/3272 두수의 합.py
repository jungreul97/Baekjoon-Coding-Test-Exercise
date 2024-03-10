import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
x = int(input())
cnt = 0

arr.sort()
start,end = 0,n-1
while start<end:
    if arr[start] + arr[end] == x:
        start+=1
        end-=1
        cnt+=1
    elif arr[start] + arr[end] < x:
        start += 1
    else:
        end -= 1

print(cnt)
