arr = list(input())
result_0 = 0
result_1 = 0
index = 0
while index<len(arr):
    start = arr[index]
    while True:
        index+=1
        if index>=len(arr):
            break
        if arr[index]!=start:
            break
    if start == '0':
        result_0+=1
    else:
        result_1+=1


if result_0<=result_1:
    print(result_0)
else:
    print(result_1)

