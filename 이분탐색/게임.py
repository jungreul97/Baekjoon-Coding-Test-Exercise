import sys
input = sys.stdin.readline

x,y = map(int,input().split())
z = int(y*100)//x

if z>=99:
    print(-1)
    exit()

start = 1
end = x
answer = 0

while start<=end:
    mid = (start+end)//2
    # print(mid,z,int((y+mid)/(x+mid)*100))
    if z>=(y+mid)*100//(x+mid):
        start = mid+1
    else:
        end = mid-1
        answer = mid
    
print(answer)

