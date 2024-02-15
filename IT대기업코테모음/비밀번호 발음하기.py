import sys
input = sys.stdin.readline
mo = ['a','e','i','o','u']
while True:
    word = input().rstrip()
    if word == 'end':
        break
    answer = True
    mocheck = False
    mo_cnt = 0
    ja_cnt = 0
    for i in range(len(word)):
        if word[i] in mo:
            mocheck  = True
            mo_cnt+=1
            ja_cnt = 0
        else:
            mo_cnt=0
            ja_cnt+=1
        if mo_cnt == 3 or ja_cnt == 3:
            answer = False
            break
        if mo_cnt == 2 and word[i] == word[i-1] and (word[i-1:i+1] != 'ee' and word[i-1:i+1] != 'oo'):
            answer = False
            break
        if ja_cnt == 2 and word[i] == word[i-1]:
            answer = False
            break
    
    if not answer or not mocheck : 
        print("<{0}> is not acceptable.".format(word))
    else:
        print("<{0}> is acceptable.".format(word))


    

        
                
                
