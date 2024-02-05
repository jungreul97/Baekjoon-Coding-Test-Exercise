import sys
input = sys.stdin.readline

s = input().rstrip()
sarr = []
narr = []
for c in s:
    if c.isalpha(): # 해당문자가 알파벳인지 확인하기
        sarr.append(c)
    else:
        narr.append(int(c))
sarr.sort()
result = ''.join(sarr)+str(sum(narr))
print(result)