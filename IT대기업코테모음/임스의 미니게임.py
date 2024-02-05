import sys
input = sys.stdin.readline
from collections import Counter

n,game = input().split()
arr = []
n = int(n)
for _ in range(n):
    arr.append(input())
set_arr = set(arr)
larr = len(set_arr)
if game == 'Y':
    print(larr)
elif game == 'F':
    print(larr//2)
else:
    print(larr//3)