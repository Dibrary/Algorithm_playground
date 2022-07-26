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