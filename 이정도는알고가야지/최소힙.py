import heapq
import sys

q = []
n = int(sys.stdin.readline().strip())

while n>0:
    cmd = int(sys.stdin.readline().strip())
    if cmd == 0:
        if len(q) == 0:
            print(0)
        else:
            number = heapq.heappop(q)
            print(number)
    else:
        heapq.heappush(q,cmd)

    n-=1

