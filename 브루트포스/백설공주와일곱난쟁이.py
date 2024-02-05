import sys
from itertools import permutations

arr = []
for _ in range(9):
    arr.append(int(input()))

cases = list(permutations(arr))

for case in cases:
    result = 0
    for j in range(7):
        result+=case[j]
    if result == 100:
        result_arr = case[:7]
        break
for i in result_arr:
    print(i)

