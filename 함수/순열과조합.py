from itertools import permutations #순열
from itertools import combinations #조합 : 순서상관없이

from itertools import product #중복 순열
from itertools import combinations_with_replacement

data = ['A','B','C']

result = list(permutations(data,3))
print("순열", result)

result2 = list(combinations(data,2))
print("조합", result2)

result3 = list(product(data,repeat=2))
print("중복 순열", result3)

result4 = list(combinations_with_replacement(data,2))
print("중복 조합", result4)

