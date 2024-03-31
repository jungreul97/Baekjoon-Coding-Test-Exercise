import sys
input = sys.stdin.readline

N = int(input())
level = []

for _ in range(N):
    level.append(int(input()))

next = level[-1]
answer = 0
for i in range(N-2,-1,-1):
    if level[i] < next:
        next = level[i]
    else:
        now = next-1
        answer += level[i]-now
        next = now

print(answer)