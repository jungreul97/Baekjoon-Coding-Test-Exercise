a = 300
b = 60
c = 10

import sys
input = sys.stdin.readline

n = int(input())

result_arr = [0,0,0]

if n>=c:
    if n>=b:
        if n>=a:
            for i in range(1,(n//a)+1):
                for j in range((n//b)+1):
                    for k in range((n//c)+1):
                        if (a*i) + (b*j) + (c*k) == n:
                            if sum(result_arr) == 0:
                                result_arr[0] = i
                                result_arr[1] = j
                                result_arr[2] = k
                            elif sum(result_arr)>i+j+k:
                                result_arr[0] = i
                                result_arr[1] = j
                                result_arr[2] = k
        else:
            for i in range(1,(n//b)+1):
                for j in range((n//c)+1):
                    if (b*i) + (c*j) == n:
                        if sum(result_arr) == 0:
                            result_arr[1] = i
                            result_arr[2] = j 
                        elif sum(result_arr)>i+j:
                            result_arr[1] = i
                            result_arr[2] = j 
    else:
        if n%c == 0:
            result_arr[2] = n%c

if sum(result_arr) == 0:
    print(-1)
else:
    for i in result_arr:
        print(i,end=' ')