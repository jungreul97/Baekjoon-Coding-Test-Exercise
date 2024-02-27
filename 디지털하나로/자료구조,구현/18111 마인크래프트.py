import sys
input = sys.stdin.readline

n,m,b = map(int,input().split())
blocks = []
min_time = int(1e9)
result_height = 0
max_h = 0
min_h = int(1e9)

for _ in range(n):
    tmp = list(map(int,input().split()))
    max_h = max(max_h,max(tmp))
    min_h = min(min_h,min(tmp))
    blocks.append(tmp)

while min_h<=max_h:
    # print("-------",min_h,"--------")
    now_b = b
    time = 0
    b_check = True
    for i in range(n):
        for j in range(m):
            now_height = blocks[i][j]
            if now_height>min_h:
                time += 2*(now_height-min_h)
                now_b+= now_height-min_h
            else:
                time += min_h - now_height
                now_b-= min_h - now_height
            # print(i,j,time,now_b)
    if now_b<0:
            b_check = False
    if b_check:
        if time <= min_time:
            min_time = time
            result_height = min_h
    # print(min_time,result_height)
    min_h+=1

print(min_time,result_height)
