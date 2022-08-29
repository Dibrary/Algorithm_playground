

# def solution(progresses, speeds):
#     need = []
#
#     for x, t in zip(progresses, speeds):
#         tmp = (100 - x) / t
#         if tmp == int(tmp):
#             need.append(int(tmp))
#         else:
#             need.append(int(tmp) + 1)
#     stack = [need.pop(0)]
#     result = []
#
#     while need:
#         value = need.pop(0)
#         if stack[-1] > value:
#             stack.append(value)
#
#         else:
#             result.append(len(stack))
#             stack = []
#             stack.append(value)
#     result.append(len(stack))
#     return result

# 위 코드 틀림.










