import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
m = int(input())
targets = list(map(int,input().split()))

dict = defaultdict(int)
for i in arr:
    dict[i]+=1
for i in targets:
    print(dict[i],end=' ')
