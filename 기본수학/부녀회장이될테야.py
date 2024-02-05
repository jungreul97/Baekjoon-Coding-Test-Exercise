t = int(input())

for i in range(t):
    k = int(input())
    b = int(input())
    if k == 0:
        print(b)
    else:
        apart = [[0 for col in range(b)] for row in range(k+1)]

        for i in range(b):
            apart[0][i] = i+1

        for i in range(1,k+1):
            for j in range(b):
                for m in range(j+1):
                    apart[i][j]+=apart[i-1][m]
        print(apart[k][b-1])
        
