import sys
from collections import deque

n = int(sys.stdin.readline().strip())
queue = deque()
for i in range(1,n+1):
    queue.append(i)

while len(queue)!=1:
    queue.popleft()
    number = queue.popleft()
    queue.append(number)

print(queue[0])