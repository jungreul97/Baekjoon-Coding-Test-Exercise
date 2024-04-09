import sys
input = sys.stdin.readline

N = int(input())
arr = []

for _ in range(N):
    word = input().rstrip()
    if not arr:
        arr.append(word)
    else:
        check = False
        for target in arr:
            if len(target) == len(word):
                for i in range(len(word)):
                    if target == word[i:]+ word[:i]:
                        check = True
                        break
            if check : break
        if not check : arr.append(word)

print(len(arr))

