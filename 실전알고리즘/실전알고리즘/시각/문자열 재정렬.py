data = input()
result=[]
value = 0

for d in data:
    if d.isalpha():#알파벳이면 문자열에 저장
        result.append(d)
    else:
        value+=int(d)

result.sort()#문자열 정렬

if value != 0:#0이 더해지는 것을 막기위해
    result.append(str(value))

print(''.join(result))#리스트를 문자열로 변환하여  출력