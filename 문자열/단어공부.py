# from string import ascii_lowercase
# s = input()
# result_index = 0
# alpha_list = list(ascii_lowercase)
# nlist = [0 for i in range(26)]

# for i in s:
#     for index in range(len(nlist)):
#         if i.lower() == alpha_list[index]:
#             nlist[index]+=1
            

# result = 0
# for i in nlist:
#     if i>int(result):
#         result = i


# answer = 0
# for i in range(len(nlist)):
#     if nlist[i] == result:
#         answer+=1
#         result_index = i

# if answer>=2:
#     print("?")
# else:
#     print(alpha_list[result_index].upper())

s = input()
s = s.upper()
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result=[]
for i in alpha:
    result.append(s.count(i))
if result.count(max(result))>1:
    print("?")
else:
    print(alpha[result.index(max(result))])