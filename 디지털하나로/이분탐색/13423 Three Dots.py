import sys
input = sys.stdin.readline

T = int(input())
while T>0:
    N = int(input())
    arr = sorted(list(map(int,input().split())))
    answer = 0
    for i in range(N-2):
        for j in range(i+2,N):
            x1,x2 = arr[i],arr[j]
            # print(x1,x2)
            start,end = i,j
            while start<=end:
                mid = (start+end)//2
                if arr[mid]-x1 == x2-arr[mid] : 
                    answer+=1
                    break
                elif arr[mid]-x1 > x2-arr[mid]:
                    end = mid-1
                else : start = mid+1
    print(answer)
    T-=1