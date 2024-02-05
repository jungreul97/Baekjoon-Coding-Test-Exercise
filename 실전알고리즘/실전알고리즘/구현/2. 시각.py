import sys
input = sys.stdin.readline
# 시, 분, 초를 하나씩 증가해서 3이 포함되는지 확인하기
n = int(input())
count = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count+=1
print(count)