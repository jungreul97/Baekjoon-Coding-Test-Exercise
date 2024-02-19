import sys
input = sys.stdin.readline

n = int(input())
answer = 0
for i in range(2, 97, 2):
    if n-i >= 4:
        answer+=(n-i-2)//2
    else:
        continue
    # print(i,(n-i-2)//2,(n-i-2)//2+2)
print(answer)