import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

result = 0
arr.sort()
for i in range(len(arr)):
    kg = arr[i]*n
    if kg>result:
        result = kg
    n-=1
print(result)