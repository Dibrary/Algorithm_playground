
'''
어떤 연산자를 가장 높은 우선순위로 놓느냐에 따라 가장 큰 값이 나올 수 있느냐; 이 말이다.

절대값이 가장 크면 된다. 즉 +-는 중요하지 않음.

총 6가지의 연산 우선순위를 정한 후에 비교해야 하는데...
'''

# def check(target): # 단순 분류용
#     if target == "*":
#         return "*"
#     elif target == "+":
#         return "+"
#     else:
#         return "-"
#
# def calc(a, b, op): # 단순 계산용
#     if op == "*":
#         return a*b
#     elif op == "+":
#         return a+b
#     else:
#         return a-b
#
# def solution(expression):
#     values = []
#     tmp = ""
#     for i in range(len(expression)):
#         if expression[i] not in "*-+":
#             tmp += expression[i]
#         else:
#             values.append(tmp)
#             tmp = ""
#             values.append(check(expression[i]))
#     values.append(tmp)
#
#     while len(values) != 1:
#         values.insert(0, str(calc(int(values.pop(0)), values.pop(0), int(values.pop(0)))))
#         print(values) # 일케 하면 앞에서부터 순차적으로 계산은 된다. 문제는 우선순위 별로 나눠서 해야 됨.


def check(target):  # 단순 분류용
    if target == "*":
        return "*"
    elif target == "+":
        return "+"
    else:
        return "-"


def calc(a, op, b): # 실제 연산만 처리용
    if op == "*":
        return int(a) * int(b)
    elif op == "+":
        return int(a) + int(b)
    else:
        return int(a) - int(b)


def product(values):
    while values.count("*") != 0:
        idx = values.index("*")
        value = str(calc(values[idx - 1], "*", values[idx + 1]))
        values.pop(idx - 1)
        values.pop(idx - 1)
        values.pop(idx - 1)
        values.insert(idx - 1, value)
    return values


def add(values):
    while values.count("+") != 0:
        idx = values.index("+")
        value = str(calc(values[idx - 1], "+", values[idx + 1]))
        values.pop(idx - 1)
        values.pop(idx - 1)
        values.pop(idx - 1)
        values.insert(idx - 1, value)
    return values


def minus(values):
    while values.count("-") != 0:
        idx = values.index("-")
        value = str(calc(values[idx - 1], "-", values[idx + 1]))
        values.pop(idx - 1)
        values.pop(idx - 1)
        values.pop(idx - 1)
        values.insert(idx - 1, value)
    return values


def case1(values):
    value = minus(add(product(values)))
    return int(value[0])


def case2(values):
    value = add(minus(product(values)))
    return int(value[0])


def case3(values):
    value = minus(product(add(values)))
    return int(value[0])


def case4(values):
    value = product(minus(add(values)))
    return int(value[0])


def case5(values):
    value = add(product(minus(values)))
    return int(value[0])


def case6(values):
    value = product(add(minus(values)))
    return int(value[0])


from copy import deepcopy


def solution(expression):
    values = []
    tmp = ""
    for i in range(len(expression)):
        if expression[i] not in "*-+":
            tmp += expression[i]
        else:
            values.append(tmp)
            tmp = ""
            values.append(check(expression[i]))
    values.append(tmp)
    return max([abs(case1(deepcopy(values))),
                abs(case2(deepcopy(values))),
                abs(case3(deepcopy(values))),
                abs(case4(deepcopy(values))),
                abs(case5(deepcopy(values))),
                abs(case6(deepcopy(values)))])


print(solution("100-200*300-500+20"))

print(solution("50*6-3*2"))

