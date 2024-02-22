import sys
from collections import defaultdict
input = sys.stdin.readline

n,m = map(int,input().split())
dict = defaultdict(int)
for _ in range(n+m):
    name = input().rstrip()
    dict[name]+=1

result = []
for i in list(dict.keys()):
    if dict[i] == 2:
        result.append(i)
result.sort()
print(len(result))
for i in result:
    print(i)


