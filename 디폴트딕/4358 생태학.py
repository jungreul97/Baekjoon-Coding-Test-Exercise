import sys
from collections import defaultdict
input = sys.stdin.readline

count = 0
result = defaultdict(int)
while True:
    name = input().rstrip()
    if not name:break
    result[name]+=1
    count+=1

result = sorted(result.items())
# print(result)
for i in result:
    print("%s %.4f" % (i[0], i[1]*100/count))