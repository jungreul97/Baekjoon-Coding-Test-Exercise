import sys

n = int(input())
result = sys.maxsize
for i in range((n//5)+1):
    for j in range((n//3)+1):
        if (i*5)+(j*3) == n:
            answer = i+j
            if answer<result:
                result = answer

if result == sys.maxsize:
    print(-1)
else:
    print(result)           
