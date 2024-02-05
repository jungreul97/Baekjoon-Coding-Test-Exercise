from re import I


def solutions(freinds,user_id):
    answer = []
    name = []
    name_friend = {}
    friend_number = {}
    
    for social in friends:
        i = social[0]
        j = social[1]
        if i == user_id:
            name.append(j)
        if j == user_id:
            name.append(i)
        if i in name_friend:
            name_friend[i].append(j)
        else: 
            name_friend[i] = [j]
        if j in name_friend:
            name_friend[j].append(i)
        else: 
            name_friend[j] = [i]
    
    for n in list(name_friend.keys()):
        friend_number[n] = 0

    for i in list(name_friend.keys()):
        if i == user_id:
            continue
        for j in name:
            if j in name_friend[i]:
                friend_number[i]+=1

    max_num = max(friend_number.values())
    
    for i in list(friend_number.keys()):
        if friend_number[i] == max_num:
            answer.append(i)
    answer.sort()
    return answer

# friends = [["david","frank"],["demi","david"],["frank","james"],["demi","james"],["claire","frank"]]
# user_id = "david"
friends = [["david","demi"],["frank","demi"],["demi","james"]]
user_id = "frank"

print(solutions(friends,user_id))
