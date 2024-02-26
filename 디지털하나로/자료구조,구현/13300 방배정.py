import sys
from collections import defaultdict
input = sys.stdin.readline

n,k = map(int,input().split())
girls = defaultdict(int)
boys = defaultdict(int)

for _ in range(n):
    a,b = map(int,input().split())
    if a == 0:
        girls[b]+=1
    else:
        boys[b]+=1

total = 0
for i in range(len(girls.values())):
    if list(girls.values())[i] % k == 0:
        total += list(girls.values())[i] // k
    else:
        total += (list(girls.values())[i] // k) + 1
for i in range(len(boys.values())):
    if list(boys.values())[i] % k == 0:
        total += list(boys.values())[i] // k
    else:
        total += (list(boys.values())[i] // k) + 1
    
print(total)