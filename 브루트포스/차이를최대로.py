import sys
from itertools import permutations
#모든경우의 배열가지수 순열 사용

n = int(input())
arr = list(map(int,input().split()))

cases = list(permutations(arr))

max_sum = 0
for case in cases:
    result = 0
    for i in range(n-1):
        result+=abs(case[i]-case[i+1])
    max_sum = max(max_sum,result)

print(max_sum)