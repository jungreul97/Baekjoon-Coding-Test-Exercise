import sys
input = sys.stdin.readline

s = input().strip()
result = []
word = []
check = False
gcheck = False

for i in range(len(s)):
    if s[i] == '<' and check:
        word.reverse()
        result.append(''.join(word))
        check = False
        gcheck = True
        word = []
        word.append(s[i])
    elif s[i] == '<' and not gcheck:
        gcheck = True
        word.append(s[i])
    elif s[i] == ' ' and gcheck:
        word.append(s[i])
    elif s[i] == ' ' and check:
        word.reverse()
        word.append(s[i])
        result.append(''.join(word))
        check = False
        word = []
    elif s[i] == ' ' and not check:
        check = True
    elif s[i] == '>' and gcheck:
        word.append(s[i])
        result.append(''.join(word))
        word = []
        gcheck = False
    elif s[i] == ' ' and check:
        word.reverse()
        word.append(s[i])
        result.append(''.join(word))
        word = []
        check = False
    elif i == len(s)-1:
        word.append(s[i])
        word.reverse()
        result.append(''.join(word))
    else:
        if check or gcheck:
            word.append(s[i])
        elif not check:
            check = True
            word.append(s[i])

print(''.join(result))