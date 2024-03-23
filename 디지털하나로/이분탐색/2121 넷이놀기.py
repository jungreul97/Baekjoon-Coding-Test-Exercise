import sys
input = sys.stdin.readline

N = int(input())
A,B = map(int,input().split())
arr = []
max_x,max_y = 0,0
min_x,min_y = int(1e9),int(1e9)
answer = 0
for _ in range(N):
    a,b = map(int,input().split())
    arr.append((a,b))
arr.sort(key = lambda x : (x[0],x[1]))

def binary_search(a,b):
    start = 0
    end = len(arr)-1
    while start<=end:
        # print(start,end,"target>>>>> ",a,b)
        mid = (start+end)//2
        # print(mid, arr[mid])
        if arr[mid][0] == a and arr[mid][1] == b: 
            # print("🚀 ~ answer:", answer)
            return True
        elif a>arr[mid][0] or (a==arr[mid][0] and b>=arr[mid][1]):
            start = mid+1
        else:
            end = mid-1
    return False


for a,b in arr:
    if binary_search(a+A,b) and binary_search(a,b+B) and binary_search(a+A,b+B):
        answer+=1
print(answer)




