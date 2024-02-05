def solutions(line1,line2):
    answer = 0
    len1 = len(line1)
    len2 = len(line2)

    space = 0
    while space*(len2-1)+len2<= len1:
        space+=1
        
        for i in range(len1-len2+1):
            s = ''
            for j in range(i,len1,space):
                s+=line1[j]
                if len(s) == len2:
                    if s == line2:
                        print(space,s)
                        answer+=1
                    else:
                        break
            if len(s) == line2:
                break
    return answer

line1 = 'abacaba'
line2 = 'acb'
print(solutions(line1,line2))