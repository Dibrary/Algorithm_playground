def solution(s):
    tmp = s.split(" ")

    result = ""
    for i in tmp:
        for idx, j in enumerate(i):
            if idx % 2 == 0:
                result += (j.upper())
            else:
                result += j
        result += (" ")
    return result[:-1]

# 틀림 아주 틀림;;

def solution(s):
    s = s.lower() # 헐 이 코드 하나 넣으니까 통과 다 됨;
    tmp = s.split(" ")

    result = ""
    for i in tmp:
        for idx, j in enumerate(i):
            if idx % 2 == 0:
                result += (j.upper())
            else:
                result += j
        result += (" ")
    return result[:-1]


# 입력에서 대, 소문자 구별 없이 들어간다거나 이런 멘트가 하나도 없으므로
# 무조건 소문자로 바꿔놓고 했어야 함.

### 다른 사람 코드 ###
def toWeirdCase(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))


### 다른 사람 코드 ###
def toWeirdCase(s):
    res = []
    for x in s.split(' '):
        word = ''
        for i in range(len(x)):
            c = x[i].upper() if i % 2 == 0 else x[i].lower()
            word = word + c
        res.append(word)
    return ' '.join(res)

