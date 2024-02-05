import sys

n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
arr2 = list(map(int,sys.stdin.readline().split()))

arr.sort()
for i in arr2:
    start = 0
    end = n-1
    incard = False
    while start<=end:
        mid = (start+end)//2
        if arr[mid] == i:
            print(1,end=' ')
            incard = True
            break
        elif arr[mid]<i:
            start = mid+1
        elif arr[mid]>i:
            end = mid-1
    if not incard:
        print(0,end=' ')    
    

        

