import sys
input = sys.stdin.readline

n = int(input())

stack = []

for _ in range(n):
    number = int(input())
    if number == 0:
        stack.pop()
    else:
        stack.append(number)

print(sum(stack))
