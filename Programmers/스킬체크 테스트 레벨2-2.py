
'''
어떤 연산자를 가장 높은 우선순위로 놓느냐에 따라 가장 큰 값이 나올 수 있느냐; 이 말이다.

절대값이 가장 크면 된다. 즉 +-는 중요하지 않음.

총 6가지의 연산 우선순위를 정한 후에 비교해야 하는데...
'''

def check(target): # 단순 분류용
    if target == "*":
        return "*"
    elif target == "+":
        return "+"
    else:
        return "-"

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

solution("100-200*300-500+20")

solution("50*6-3*2")

