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









