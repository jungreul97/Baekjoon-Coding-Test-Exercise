a,b = input().split()

num1 = a[::-1]
num2 = b[::-1]

if num1<num2:
    print(num2)
else:
    print(num1)
