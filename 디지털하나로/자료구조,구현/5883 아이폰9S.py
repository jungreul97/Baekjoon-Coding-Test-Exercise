import sys
from collections import deque
input = sys.stdin.readline


N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

answer = 0
for i in range(N):
    start = arr[i]
    tmp = []
    cnt = 1
    # print(i, "start>>>>", start)
    for j in range(i+1,N):
        if start == arr[j] : cnt += 1
        elif not tmp : tmp.append(arr[j])
        elif tmp and tmp[0] == arr[j]: continue
        else : break
        # print(tmp, cnt )
    answer = max(answer,cnt)
print(answer)



