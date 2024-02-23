import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
target = int(input())
answer = 0

for i in arr:
    if target == i:
        answer += 1
print(answer)