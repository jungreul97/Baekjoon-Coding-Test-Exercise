from string import ascii_lowercase

s = input()
result_arr = [-1 for i in range(26)]
alpha_list = list(ascii_lowercase)

for s_index in range(len(s)):
    for index in range(len(alpha_list)):
        if s[s_index] == alpha_list[index]:
            if result_arr[index] != -1:
                continue
            else:
                result_arr[index] = s_index 

for i in result_arr:
    print(i,end=" ")