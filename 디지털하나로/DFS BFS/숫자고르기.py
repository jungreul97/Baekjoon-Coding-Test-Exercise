import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = []
arr.append([i for i in range(1,n+1)])
tmp = []
for _ in range(n):
    tmp.append(int(input()))
arr.append(tmp)
print(arr)

