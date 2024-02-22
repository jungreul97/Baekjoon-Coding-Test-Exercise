import sys
input = sys.stdin.readline

steel = input().rstrip()
now = 0
answer = 0
first = 0
for i in range(len(steel)):
    if steel[i] == '(':
        now+=1
    else:
        if steel[i-1] == '(':
            now-=1
            answer+=now
            if now>first:
                answer += (now-first)
            first = now
        else:
            now-=1
            first-=1
    # print(i,answer)

print(answer)
# ()(((()())(())()))(())
# (((()(()()))(())()))(()())

# 17 24

ir= input()
stack=[]
cnt = 0
for i in range(len(ir)):
    if ir[i] == "(":
        stack.append("(")
    else :
        if ir[i-1]=="(":
            stack.pop()
            cnt+=len(stack) # 첫 번째 경우인 현재의 쇠막대기들을 카운팅합니다.
            
        else :
            stack.pop()
            cnt+=1 # 이 부분은 두 번째 경우인 나머지 부분을 세는 것입니다.
print(cnt)