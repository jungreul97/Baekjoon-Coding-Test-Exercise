import sys
input = sys.stdin.readline

n = int(input())
dict = {}

for _ in range(n):
    name,command = map(str,input().strip().split())
    dict[name] = command

answer = []

for key,value in dict.items():
    if value == 'enter':
        answer.append(key)

answer.sort(reverse = True)

for i in answer:
    print(i)