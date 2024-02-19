import sys
input = sys.stdin.readline

arr = []
for _ in range(10):
    arr.append(int(input()))

answer = 0
for i in arr:
    if answer+i == 100:
        answer = answer+i
        break
    elif answer+i<100:
        answer += i
    else:
        tmp = answer+i
        if tmp - 100 < 100 - answer or tmp - 100 == 100 - answer:
            answer = tmp
        break
print(answer)