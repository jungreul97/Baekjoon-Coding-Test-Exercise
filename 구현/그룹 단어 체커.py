import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(input().strip())

result = 0

for word in arr:
    check = True
    checklist = []
    for i in range(len(word)):
        if word[i] not in checklist:
            checklist.append(word[i])
        elif i!=0 and word[i] == word[i-1]:
            continue
        else:
            check = False
    if check:
        result+=1

print(result)