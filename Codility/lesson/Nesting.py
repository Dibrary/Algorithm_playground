from collections import deque

def solution(S):
    if S.count("(") == S.count(")"): # 괄호의 갯수로 먼저 필터링
        table = {")":"("}
        stack = deque()
        S = S.replace("()","")

        for x in S:
            if len(stack) == 0:
                stack.append(x)
            if x in table:
                stack.pop()
        return 1 if len(stack) == 0 else 0
    else:
        return 0

# ()) 예제가 통과하면 안 된다. 100%.

print(solution("(()(())())"))
print(solution("())"))