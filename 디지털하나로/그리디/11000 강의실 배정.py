import sys,heapq
input = sys.stdin.readline

N = int(input())
times = []
for _ in range(N):
    start,end = map(int,input().split())
    times.append((start,end))

times.sort()

answer = 0
end_times = []
for time in times:
    start,end = time
    if not end_times:
        end_times.append(end)
        answer+=1
    elif start < end_times[0]:
        answer += 1
        heapq.heappush(end_times,end)
    else:
        heapq.heappop(end_times)
        heapq.heappush(end_times,end)
print(answer)