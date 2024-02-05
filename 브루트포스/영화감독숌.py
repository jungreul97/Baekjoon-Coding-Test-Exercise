n = int(input())

order_list = []

i=665
while len(order_list)<=10000:
    i+=1
    if '666' in str(i):
        order_list.append(i)
    else:
        continue

print(order_list[n-1])