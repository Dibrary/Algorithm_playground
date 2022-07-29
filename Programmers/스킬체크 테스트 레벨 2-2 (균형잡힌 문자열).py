# from copy import deepcopy
#
#
# def change(stack):
#     for v in stack:
#         if v[1] == "(":
#             v[1] = ")"
#         elif v[1] == ")":
#             v[1] = "("
#     return stack
#
#
# def check(p):
#     tb = {")": "("}
#
#     stack = []
#     cnt = 0
#
#     for idx, k in enumerate(p):
#         if k not in tb:
#             stack.append([idx, k])
#         else:
#             if stack != [] and stack[-1][1] == tb[k]:
#                 stack.pop()
#             else:
#                 stack.append([idx, k])
#     return stack
#
#
# def solution(p):
#     if p == "":
#         return ""
#
#     stack = check(p)
#     if stack == []:
#         return p
#     else:
#         stack = change(stack)
#         tmp = list(deepcopy(p))
#
#         for i in stack:
#             tmp[i[0]] = i[1]
#         stack = check(tmp)
#         if stack == []:
#             return "".join(map(str, tmp))
#         else:
#             # 여기서 else로 빠져버리면 다시 위 작업들을 반복해야 하는데,



from copy import deepcopy

def change(stack): # 재귀적으로 수행해서 문자열을 붙인다는데, 그냥 이렇게 일괄적으로 변환하면 안되는듯.
    for v in stack:
        if v[1] == "(":
            v[1] = ")"
        elif v[1] == ")":
            v[1] = "("
    return stack


def check(p):
    tb = {")": "("}

    stack = []
    cnt = 0

    for idx, k in enumerate(p):
        if k not in tb:
            stack.append([idx, k])
        else:
            if stack != [] and stack[-1][1] == tb[k]:
                stack.pop()
            else:
                stack.append([idx, k])
    return stack


def solution(p):
    if p == "":
        return ""

    stack = check(p)
    if stack == []:
        return p
    else:
        while stack != []:
            stack = change(stack)
            tmp = list(deepcopy(p))

            for i in stack:
                tmp[i[0]] = i[1]
            stack = check(tmp)
        return "".join(map(str, tmp))

# 위 코드는 5개 맞음 =_=;; 25개 중에;

## 책 풀이 ##

def balanced_index(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i

def check_proper(p):
    count = 0
    for i in p:
        if i == '(':
            count += 1
        else:
            if count == 0:
                return False
            count -= 1
    return True

def solution(p):
    answer = ''
    if p == '':
        return answer
    index = balanced_index(p)
    u = p[:index + 1]
    v = p[index + 1:]

    if check_proper(u):
        answer = u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer