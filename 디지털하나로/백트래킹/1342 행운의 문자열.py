import sys
from collections import Counter
input = sys.stdin.readline

answer = 0
s = input().rstrip()
dict = Counter(s)
chars = []

def dfs():
    global answer
    if len(chars) == len(s):
        # print(chars)
        answer += 1
    
    for key in dict.keys():
        if (len(chars) > 0 and key == chars[-1]) or dict[key] == 0:
            continue
        
        dict[key] -= 1
        chars.append(key)
        dfs()
        chars.pop()
        dict[key]+=1

dfs()
print(answer)