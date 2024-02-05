n = int(input())
arr = []
for i in range(n):
    arr.append(input())
result_arr = []

for str in arr:
    result = 0
    point = 0
    for i in str:
        if i == 'O':
            point+=1
            result+=point
        elif i == 'X':
            
            point=0
    result_arr.append(result)

for number in result_arr:
    print(number)

