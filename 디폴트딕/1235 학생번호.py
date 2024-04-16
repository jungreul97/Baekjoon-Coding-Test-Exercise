import sys
from collections import defaultdict
input = sys.stdin.readline


N = int(input())
arr = []
for _ in range(N):
    arr.append(input().rstrip())
answer = 0
for i in range(1,len(arr[0])+1):
    dict = defaultdict(int)
    for j in range(N):
        dict[arr[j][-i:]] += 1
    if len(dict.keys()) == N : 
        answer = i
        break

print(answer)


