import sys
from collections import defaultdict
input = sys.stdin.readline

start,end,streaming_end = map(str,input().split())
start = 60*int(start[:2])+int(start[3:])
end = 60*int(end[:2])+int(end[3:])
streaming_end = 60*int(streaming_end[:2])+int(streaming_end[3:])

dict = defaultdict(bool)
answer = []

while True:
    try:
        time,name = map(str,input().rstrip().split())
        time = 60*int(time[:2])+int(time[3:])
        if time <= start:
            dict[name] = True
        if end<= time <= streaming_end and dict[name]: answer.append(name)
    except:
        break

set_answer = list(set(answer))
print(len(set_answer))
