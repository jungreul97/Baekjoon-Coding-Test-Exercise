import sys
from itertools import permutations

n = int(sys.stdin.readline())
arr = [i for i in range(1,n+1)]

cases = list(permutations(arr))

for case in cases:
    for i in case:
        print(i,end = ' ')
    print()

