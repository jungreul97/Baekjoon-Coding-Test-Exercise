import sys
input = sys.stdin.readline

N = int(input())

answer = 0
arr = []
for _ in range(N):
    start,end = map(int,input().split())
    arr.append((start,end))

arr.sort(key = lambda x : (x[0],x[1]))
# print(arr)
max_n = 0
for start,end in arr:
    if max_n <= start: 
        answer += (end-start)
        max_n = end
    elif start<max_n and max_n<end:
        answer += (end-max_n)
        max_n = end

print(answer)