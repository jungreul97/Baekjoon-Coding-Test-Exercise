import sys
input = sys.stdin.readline

n = int(input())
target = list(input().rstrip())
result = 0

for _ in range(n-1):
    compare = target.copy()
    word = input().rstrip()
    cnt = 0

    for w in word:
        if w in compare:
            compare.remove(w)
        else:
            cnt+=1
    if cnt<2 and len(compare)<2:
        result+=1
print(result)
