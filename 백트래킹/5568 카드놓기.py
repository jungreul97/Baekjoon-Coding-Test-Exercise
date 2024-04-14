import sys
from collections import deque
input = sys.stdin.readline


n = int(input())
k = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

answer = []
numbers = []
visited = [False] * n

def dfs():
    if len(numbers) == k:
        answer.append(''.join(numbers))
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            numbers.append(str(arr[i]))
            dfs()
            visited[i] = False
            numbers.pop()

dfs()
set_numbers = list(set(answer))
print(len(set_numbers))

