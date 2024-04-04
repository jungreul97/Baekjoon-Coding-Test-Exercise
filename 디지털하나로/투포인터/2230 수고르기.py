import sys
input = sys.stdin.readline

N,M = map(int,input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))

arr.sort()
answer = 2000000000
start,end = 0,1
while end < N:
        result = arr[end] - arr[start]
        if result < M:
              end += 1
        elif result > M:
              start += 1
              answer = min(result,answer)
        else:
              answer = M
              break

print(answer)