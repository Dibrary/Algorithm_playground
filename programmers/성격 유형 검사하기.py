
def solution(survey, choices):
    left = [0, 3, 2, 1]
    right = [0, 0, 0, 0, 0, 1, 2, 3]

    table = dict()
    for n in "RTCFJMAN":
        table[n] = 0

    for idx, x in enumerate(survey):
        if choices[idx] < 4:
            table[x[0]] += left[choices[idx]]
        elif choices[idx] > 4:
            table[x[1]] += right[choices[idx]]

    result = ""
    type = [["R","T"],["C","F"],["J","M"],["A","N"]]
    for i in range(4):
        if table[type[i][0]] > table[type[i][1]]:
            result += type[i][0]
        elif table[type[i][0]] < table[type[i][1]]:
            result += type[i][1]
        else:
            type[i].sort()
            result += type[i][0]

    return result


## 다른 사람 코드 ##

def solution(survey, choices):

    my_dict = {"RT":0,"CF":0,"JM":0,"AN":0}
    for A,B in zip(survey,choices):
        if A not in my_dict.keys():
            A = A[::-1]
            my_dict[A] -= B-4
        else:
            my_dict[A] += B-4

    result = ""
    for name in my_dict.keys():
        if my_dict[name] > 0:
            result += name[1]
        elif my_dict[name] < 0:
            result += name[0]
        else:
            result += sorted(name)[0]

    return result








def solution(survey, choices):
    answer = ''
    RTCFJMAN = [0,0,0,0,0,0,0,0]
    str = "RTCFJMAN"
    for i in range(len(survey)):
        RTCFJMAN[str.index(survey[i][1])] += choices[i]-4

    if(RTCFJMAN[0]>=RTCFJMAN[1]): answer+= "R"
    else: answer+="T"
    if(RTCFJMAN[2]>=RTCFJMAN[3]): answer+= "C"
    else: answer+="F"
    if(RTCFJMAN[4]>=RTCFJMAN[5]): answer+= "J"
    else: answer+="M"
    if(RTCFJMAN[6]>=RTCFJMAN[7]): answer+= "A"
    else: answer+="N"


    return answer
