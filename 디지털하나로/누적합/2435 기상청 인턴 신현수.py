import sys
input = sys.stdin.readline

n,k = map(int,input().split())
temps = list(map(int,input().split()))

answer = []

for i in range(n-k+1):
    answer.append(sum(temps[i:i+k]))
    print(temps[i:i+k])
print(max(answer))