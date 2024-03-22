import sys
input = sys.stdin.readline

A,B = map(str,input().split())
answer = 0
if len(A) == len(B):
    for i in range(len(A)):
        if A[i] != B[i] : answer+=1
elif A in B : 
    print(0)
    exit()
else:
    min_num = int(1e9)
    start = 0
    end = len(A)
    while end<=len(B):
        result = 0
        # print(B[start:end])
        for i in range(len(A)):
            if A[i] != B[start:end][i]: result += 1
        min_num = min(min_num,result)
        start+=1
        end+=1
    answer = min_num

print(answer)

