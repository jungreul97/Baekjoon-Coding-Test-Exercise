def solutions(rows,columns,swipes):
    answer = []
    arr = []
    for i in range(1,rows+1):
        t = [(i-1)*columns+j for j in range(1,columns+1)]
        arr.append(t)
    
    for swipe in swipes:
        d,r1,c1,r2,c2 = swipe[0],swipe[1]-1,swipe[2]-1,swipe[3]-1,swipe[4]-1
        sum = 0
        part_arr = []
        if d == 1:
            for i in range(c1,c2+1):
                sum+=arr[r2][i]
                part_arr.append(arr[r2][i])
            answer.append(sum)
            for i in range(r2,r1,-1):
                for j in range(c1,c2+1):
                    arr[i][j] = arr[i-1][j]
            for i in range(c1,c2+1):
                arr[r1][i] = part_arr[0]
                del part_arr[0]
            print(arr)
        elif d == 2:
            for i in range(c1,c2+1):
                sum+=arr[r1][i]
                part_arr.append(arr[r1][i])
            answer.append(sum)
            for i in range(r1,r2):
                for j in range(c1,c2+1):
                    arr[i][j] = arr[i+1][j]
            for i in range(c1,c2+1):
                arr[r2][i] = part_arr[0]
                del part_arr[0]
            print(arr)
        elif d == 3:
            for i in range(r1,r2+1):
                sum+=arr[i][c2]
                part_arr.append(arr[i][c2])
            answer.append(sum)
            for i in range(c2,c1,-1):
                for j in range(r1,r2+1):
                    arr[j][i] = arr[j][i-1]
            for i in range(r1,r2+1):
                arr[i][c1] = part_arr[0]
                del part_arr[0]
            print(arr)
        else:
            for i in range(r1,r2+1):
                sum+=arr[i][c1]
                part_arr.append(arr[i][c1])
            answer.append(sum)
            for i in range(c1,c2):
                for j in range(r1,r2+1):
                    arr[j][i] = arr[j][i+1]
            for i in range(r1,r2+1):
                arr[i][c2] = part_arr[0]
                del part_arr[0]
            print(arr)
    return answer


# rows = 4
# columns = 3
# swipes = [[1,1,2,4,3],[3,2,1,2,3],[4,1,1,4,3],[2,2,1,3,3]]
# rows = 2
# columns = 4
# swipes = [[3,1,2,2,4],[3,1,2,2,4],[4,2,1,2,3],[1,1,1,2,3]]
rows = 2
columns = 2
swipes = [[3,1,1,1,2],[1,1,2,2,2],[4,2,1,2,2],[2,1,1,2,1]]


print(solutions(rows,columns,swipes))