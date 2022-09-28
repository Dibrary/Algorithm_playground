

from collections import deque

def solution(S):
    table = {"}":"{",
             "]":"[",
             ")":"("}

    stack = deque()
    for x in S:
        if len(stack) == 0:
            stack.append(x)
        if x in table and stack[-1] == table[x]:
            stack.pop()
    return 1 if len(stack) == 0 else 0

# 위 코드는 50% 받은 코드


print(solution("{[()()]}"))




