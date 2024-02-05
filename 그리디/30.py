import sys
input = sys.stdin.readline

s = input().rstrip()
if not '0' in s:
    print(-1)
else:
    sum = 0
    for i in range(len(s)):
        sum+=int(s[i])
    if sum%3 != 0:
        print(-1)
    else:
        arr = []
        for i in range(len(s)):
            arr.append((s[i]))
        arr.sort(reverse = True)
        result = ''.join(arr)
        print(result)