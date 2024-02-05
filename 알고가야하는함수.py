import sys
input = sys.stdin.readline

#eval : 수식을 숫자로 바꿔주는 함수
result = eval("(3+5)*7") 
print(result) # 56

#Counter : 등장횟수를 세는 기능을 제공함
from collections import Counter
counter = Counter(['red','blue','red','green','blue','blue'])
print(counter) # Counter({'blue': 3, 'red': 2, 'green': 1})
print(dict(counter)) # {'red': 2, 'blue': 3, 'green': 1}
print(counter['blue']) # 3
print(counter['green']) # 1

#gcd : 최대공약수, lcm : 최소공배수
import math
def lcm(a,b):
    return a*b // math.gcd(a,b)
print(math.gcd(21,14)) # 7
print(lcm(21,14)) # 42 

# isalpha() : 해당문자가 알파벳인지 확인하는 함수
print('c'.isalpha()) # True

#ceil(올림),floor(버림),round(반올림)
print(math.ceil(99.2)) # 100
print(math.floor(99.2)) # 99
print(round(99.2)) # 99
