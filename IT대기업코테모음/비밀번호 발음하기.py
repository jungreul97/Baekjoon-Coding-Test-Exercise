import sys
input = sys.stdin.readline

check = ['a','e','i','o','u']
while True:
    s = input().rstrip()
    mo = 0
    ja = 0
    mo_check = True
    s2 = ''
    for c in s:
        mo_check = False
        s2.append(c)
        if len(s2) == 2:
            if s == 'ee' or s== 'oo':
                mo_check = False