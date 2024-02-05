n = int(input())
money = 1000-n
result = int(1e9)
for i in range(3):
    for j in range(5):
        for k in range(2):
            for l in range(5):
                for m in range(2):
                    for n in range(5):
                        if (500*i)+(100*j)+(50*k)+(10*l)+(5*m)+n == money:
                            if i+j+k+l+m+n<result:
                                result = i+j+k+l+m+n

print(result)