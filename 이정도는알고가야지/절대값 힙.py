import heapq
import sys

n = int(sys.stdin.readline().strip())
q=[]
while n>0:
    cmd = int(sys.stdin.readline().strip())
    if cmd == 0:
        if len(q) == 0:
            print(0)
        else:
            a,b = heapq.heappop(q)
            print(b)
    else:
        heapq.heappush(q,(abs(cmd),cmd))

    n-=1
