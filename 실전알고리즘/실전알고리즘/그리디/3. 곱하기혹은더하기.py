import sys
input = sys.stdin.readline

number = input().rstrip()
result = 0
for n in number:
    if result <=1 or int(n) <=1:
        result+=int(n)
    else:
        result*=int(n)

print(result)
