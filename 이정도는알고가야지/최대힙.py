import heapq
import sys

q = []
n = int(sys.stdin.readline().strip())

while n>0:
    cmd = sys.stdin.readline().strip()
    if int(cmd) == 0:
        if len(q) == 0:
            print(0)
        else:
            number = heapq.heappop(q)
            number = abs(number)
            print(number)
    else:
        cmd = '-'+cmd
        heapq.heappush(q,int(cmd))

    n-=1
