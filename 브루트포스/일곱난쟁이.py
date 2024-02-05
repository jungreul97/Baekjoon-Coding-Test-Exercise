import sys
from itertools import permutations

arr=[]
for _ in range(9):
    arr.append(int(input()))

cases = list(permutations(arr))

answer=[]
for case in cases:
    result = 0
    for i in range(7):
        result+=case[i]
    if result == 100:
        for j in range(7):
            answer.append(case[j])
        break
answer.sort()
for i in answer:
    print(i)

