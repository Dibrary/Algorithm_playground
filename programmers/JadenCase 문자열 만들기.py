
# def solution(s):
#     tmp = [x.lower() for x in s.split(" ")]
#     result = []
#     for x in tmp:
#         if x[0].isalpha():
#             result.append(x[0].upper()+x[1:])
#         else:
#             result.append(x)
#     return " ".join(map(str, result))

# 위 코드 44.4점 받은 코드.
# 문제 조건 중에 '공백이 연속으로 있을 수 있다' 라고 해서 공백을 많이 넣어보니
# IndexError: string index out of range 이 에러가 난다. 그래서 런타임 에러가 난듯.


def solution(s):
    tmp = [x.lower() for x in s.split(" ")]
    result = []
    for x in tmp:
        if x == '':
            result.append(x)
        elif x[0].isalpha():
            result.append(x[0].upper()+x[1:])
        else:
            result.append(x)
    return " ".join(map(str, result))

print(solution("3people unFollowed me"))

## 다른 사람 코드 ##

def Jaden_Case(s):
    return s.title()





def Jaden_Case(s):
    s = ' '.join(((word[0].upper()) + word[1:].lower()) for word in s.split())
    return s

