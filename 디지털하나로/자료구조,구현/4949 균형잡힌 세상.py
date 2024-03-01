import sys
input = sys.stdin.readline

while True:
    sent = input().rstrip()
    if sent == '.':
        break
    stack = []
    check = True
    for i in sent:
        if i == "(" or i == "[":
            stack.append(i)
        elif i == ")":
            if len(stack) == 0 or stack[-1] != "(":
                check = False
                break
            else:
                stack.pop()
        elif i == "]":
            if len(stack) == 0 or stack[-1] != "[":
                check = False
                break
            else:
                stack.pop()
        if not check: break
        # print(i,stack)
    if stack or not check:
        print("no")
    else:
        print("yes")
        