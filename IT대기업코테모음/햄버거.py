import sys
input = sys.stdin.readline

n,k = map(int,input().split())
list  = list(map(str,input().rstrip()))
result = 0

for i in range(n):
    if list[i] == 'P':
        for j in range(max(i-k,0),min(i+k+1,n)):
            if list[j] == 'H':
                list[j] = 'T'
                result+=1
                break

print(result)
