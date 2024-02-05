import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
arr.sort()

result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모함가의 수

for i in arr:
    count+=1
    if i>=count:
        result+=1
        count = 0
print(result)

