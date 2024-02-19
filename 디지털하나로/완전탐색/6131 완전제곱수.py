import sys
input = sys.stdin.readline

answer = 0

n = int(input())
for i in range(1,501):
    for j in range(2,501):
        if j**2 - i**2 == n:
            answer+=1
        if j**2 - i**2 >n:
            continue
print(answer)