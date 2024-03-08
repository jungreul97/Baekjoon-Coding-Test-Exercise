import sys
input = sys.stdin.readline

N,M = map(int,input().split())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
answer = []

idx1,idx2 = 0,0
while idx1<N and idx2<M:
    if arr1[idx1]<=arr2[idx2] : 
        answer.append(arr1[idx1])
        idx1+=1
    else:
        answer.append(arr2[idx2])
        idx2+=1
while idx1<N:
    answer.append(arr1[idx1])
    idx1+=1
while idx2<M:
    answer.append(arr2[idx2])
    idx2+=1
print(*answer)
