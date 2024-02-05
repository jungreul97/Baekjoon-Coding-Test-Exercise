import sys
input = sys.stdin.readline
from itertools import permutations

n = int(input())
numbers = list(map(int,input().split()))
calcs = list(map(int,input().split()))

calc = []

for i in range(4):
    if calcs[i]>0:
        if i == 0:
            for _ in range(calcs[i]):
                calc.append('+')
        elif i == 1:
            for _ in range(calcs[i]):
                calc.append('-')
        elif i == 2:
            for _ in range(calcs[i]):
                calc.append('*')
        elif i == 3:
            for _ in range(calcs[i]):
                calc.append('/')

cases = list(permutations(calc))
max_result = 0
min_result = int(1e9)
rank = 0
for case in cases:
    result = numbers[0]
    calc_index = 0
    for i in range(1,len(numbers)):
        if case[calc_index] == '+':
            result+=numbers[i]
        elif case[calc_index] == '-':
            result-=numbers[i]
        elif case[calc_index] == '*':
            result*=numbers[i]
        elif case[calc_index] == '/':
            if result<0 and numbers[i]>0:
                result = abs(result)
                result//=numbers[i]
                result = 0-abs(result)
            else:
                result//=numbers[i]

        calc_index+=1

    if result>max_result:
        max_result = result
    if result<min_result:
        min_result = result

print(max_result)
print(min_result)
    

            


