import sys
from collections import defaultdict

input = sys.stdin.readline

arr = [1, 5, 10, 50]
numbers = []
dict = defaultdict(int)

N = int(input())

def dfs(start):
    if len(numbers) == N:
        dict[sum(numbers)] += 1
        return
    for i in range(start,4):
        numbers.append(arr[i])
        dfs(i)
        numbers.pop()
dfs(0)
print(len(dict))