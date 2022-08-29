# from collections import deque
#
# def solution(s):
#     if len(s) == 1:
#         return 0
#
#     stack = deque()
#     stack.append(s[0])
#     idx = 1
#
#     while stack and idx < len(s):
#
#         if stack[-1] == s[idx]:
#             stack.pop()
#         else:
#             stack.append(s[idx])
#         idx += 1
#     if len(stack) != 0:
#         return 0
#     else:
#         return 1

# 효율성 테스트 모두 통과. 정확성 테스트에서 4개 틀림.
# 반례로 뭐가 있는지 잘 모르겠음. "abccaabaa"
# 맨 마지막에 stack[-1] == s[idx] 부분에서 pop해 버리고 while 빠져나오면 return은 1이 되어버림.

# from collections import deque
#
# def solution(s):
#     if len(s) == 1:
#         return 0
#
#     stack = deque()
#     stack.append(s[0])
#     idx = 1
#
#     while stack and idx < len(s)-1:
#         if stack[-1] == s[idx]:
#             stack.pop()
#         else:
#             stack.append(s[idx])
#         idx += 1
#     if stack:
#         if stack[-1] == s[idx]:
#             stack.pop()
#         if len(stack) != 0:
#             return 0
#         else:
#             return 1
#     else:
#         return 0

# 위 코드 처럼 수정하자니, stack이 비어버리면 바로 while문을 탈출해버린다.

from collections import deque

def solution(s):
    if len(s) == 1:
        return 0

    stack = deque()
    stack.append(s[0])
    idx = 1

    while idx < len(s)-1: # stack이 비었는지 확인을 여기서 안하고
        if stack: # 여기서 하게 함.
            if stack[-1] == s[idx]:
                stack.pop()
            else:
                stack.append(s[idx])
        else:
            stack.append(s[idx])
        idx += 1
    if stack:
        if stack[-1] == s[idx]:
            stack.pop()
        if len(stack) != 0:
            return 0
        else:
            return 1
    else:
        return 0

# 통과



## 다른 사람 코드 ##
def solution(s):
    answer = []
    for i in s:
        if not(answer):
            answer.append(i)
        else:
            if(answer[-1] == i):
                answer.pop()
            else:
                answer.append(i)
    return not(answer)












def solution(s):
    stack = []
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    if len(stack) == 0:
        return 1
    else:
        return 0











def solution(s):
    stack = []
    for i in s:
        stack.append(i)
        while True:
            try:
                if stack[-1] == stack[-2]:
                    stack.pop()
                    stack.pop()
                else:
                    break
            except:
                break
    return not stack