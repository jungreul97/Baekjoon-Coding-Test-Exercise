import sys
input = sys.stdin.readline

while True:
    arr = list(map(int,input().split()))
    arr.sort()
    if sum(arr) == 0:
        break
    elif arr[0] == arr[1] == arr[2]:
        print("Equilateral")
    elif arr[0]+arr[1]<=arr[2]:
        print("Invalid")
    elif arr[0] == arr[1] or arr[1] == arr[2]:
        print("Isosceles")
    else:
        print("Scalene")
    