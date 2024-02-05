a = []
max_num = 0
num = 0
for i in range(9):
    num = int(input())
    a.append(num)
    if num > a[max_num]:
        max_num = i

print(a[max_num])
print(max_num+1)