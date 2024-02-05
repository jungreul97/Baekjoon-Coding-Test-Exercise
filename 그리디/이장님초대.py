import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

arr.sort(reverse = True)

result = arr[0]

if n == 1:
    print(result+2)
else:
    for i in range(1,n):
        if result<(i+arr[i]):
            result = i+arr[i]
    
    result+=2
    print(result)