import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

arr.sort()

zero_idx = 0
for i in range(N):
    if arr[i]>0:
        zero_idx = i
        break
if zero_idx == 0 and arr[0] <= 0:
    minus_arr = arr
    plus_arr = []
else:
    minus_arr = arr[:zero_idx]
    plus_arr = arr[zero_idx:]
# print(minus_arr)
# print(plus_arr)


answer = 0
if minus_arr:
    if len(minus_arr) % 2 == 0 and minus_arr[-1] == 0:
        for i in range(0,len(minus_arr)-2,2):
            answer += (minus_arr[i]*minus_arr[i+1])
    elif len(minus_arr) % 2 == 0:
        for i in range(0,len(minus_arr)-1,2):
            answer += (minus_arr[i]*minus_arr[i+1])
    else:
        for i in range(0,len(minus_arr)-1,2):
            answer += (minus_arr[i]*minus_arr[i+1])
        answer += minus_arr[-1]
# print("minus",answer)
if plus_arr:
    if len(plus_arr) % 2 == 0:
        for i in range(len(plus_arr)-1,0,-2):
            if plus_arr[i] != 1 and plus_arr[i-1] != 1:
                answer += (plus_arr[i]*plus_arr[i-1])
            else:
                answer += (plus_arr[i]+plus_arr[i-1])
    else:
        for i in range(len(plus_arr)-1,1,-2):
            if plus_arr[i] != 1 and plus_arr[i-1] != 1:
                answer += (plus_arr[i]*plus_arr[i-1])
            else:
                answer += (plus_arr[i]+plus_arr[i-1])
        answer += plus_arr[0]
print(answer)



