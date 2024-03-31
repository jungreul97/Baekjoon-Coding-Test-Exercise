import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int,input().split())
nums = []
for _ in range(n):
     nums.append(int(input()))

queue = deque()
queue.append(0)
answer = 0
while queue:
    x = queue.popleft()
    if x == k :
         answer += 1
    if x > k:
         continue
    for num in nums:
         queue.append(x+num)

print(answer)
