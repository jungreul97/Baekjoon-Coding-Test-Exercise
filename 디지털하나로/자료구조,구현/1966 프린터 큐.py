import sys
import heapq
from collections import deque
input = sys.stdin.readline

k = int(input())
while k>0:
    answer = 0
    n,m = map(int,input().split())
    papers = list(map(int,input().split()))
    stack = deque()
    q = []
    for i in range(len(papers)):
        stack.append((papers[i],i))
        heapq.heappush(q, -papers[i])
    # print(stack)
    # print(q)
    # print("------",k)
    while stack:
        now_max_num = -1*heapq.heappop(q)
        now_paper,idx = stack.popleft()
        # print(now_max_num)
        # print(now_paper,idx)
        if  now_max_num == now_paper and idx == m:
            answer+=1
            break
        elif now_max_num == now_paper:
            answer+=1
            continue
        else:
            stack.append((now_paper,idx))
            heapq.heappush(q,-now_max_num)
    print(answer)
    k-=1
