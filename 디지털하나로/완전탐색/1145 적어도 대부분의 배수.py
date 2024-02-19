import sys
input = sys.stdin.readline

a,b,c,d,e = map(int,input().split())
min = min(a,b,c,d,e)
while True:
    result = 0
    if min%a == 0:
        result+=1
    if min%b == 0:
        result+=1
    if min%c == 0:
        result+=1
    if min%d == 0:
        result+=1
    if min%e == 0:
        result+=1
    if result >= 3:
        print(min)
        break
    min+=1
    