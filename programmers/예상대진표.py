
# 2의 20승이라고 해도 1048576밖에 안 됨.

# def solution(n, a, b):
#     arr = [x for x in range(1, n+1)]
#
#     tmp = []
#     cnt = 1
#
#     while abs(arr.index(a) - arr.index(b)) != 1:
#         for x in range(0, len(arr)-1, 2):
#             if a in arr[x:x+2]:
#                 tmp.append(a)
#             elif b in arr[x:x+2]:
#                 tmp.append(b)
#             else:
#                 tmp.append(arr[x])
#         arr = tmp
#         tmp = []
#         cnt += 1
#     return cnt
#
# print(solution(8, 4, 7))

# 위 코드 4개 틀림.














