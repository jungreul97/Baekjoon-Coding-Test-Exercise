n,m = map(int,input().split())
arr = []
for i in range(n):
    arr.append(input())

result = 2500


for i in range(n-7):
    for j in range(m-7):
        first_b_sum = 0
        first_w_sum = 0
        for k in range(i,i+8):
            for l in range(j,j+8):
                if (k+l)%2==0:
                    if arr[k][l] != 'B':
                        first_b_sum+=1
                    if arr[k][l] !='W':
                        first_w_sum+=1
                else:
                    if arr[k][l] != 'B':
                        first_w_sum+=1
                    if arr[k][l] !='W':
                        first_b_sum+=1
        if first_b_sum<first_w_sum:
            if first_b_sum<result:
                result = first_b_sum
        else:
            if first_w_sum<result:
                result = first_w_sum

print(result)





        