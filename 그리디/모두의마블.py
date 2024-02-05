import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().rstrip().split()))
arr.sort()

result = 0
level = arr[-1]
result = sum(arr[:-1])
result+=level*(n-1)
print(result)

