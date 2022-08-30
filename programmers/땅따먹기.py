
# def solution(land):
#     result = max(land[0])
#     idx = land[0].index(result)
#
#     for i in range(1, len(land)):
#         if land[i].index(max(land[i])) == idx:
#             tmp = sorted(land[i], reverse=True)
#             result += tmp[1]
#             idx = land[i].index(tmp[1])
#         else:
#             result += max(land[i])
#             idx = land[i].index(max(land[i]))
#     return result
#
# print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))

# 위 코드는 예제만 통과하지 모조리 실패함.

# def solution(land):
#     result = max(land[0])
#     idx = land[0].index(result)
#     for x in range(1, len(land)):
#         while land[x].index(max(land[x])) == idx:
#             land[x][idx] = 0
#         result += max(land[x])
#         idx = land[x].index(max(land[x]))
#     return result

# 위 코드도 모조리 실패함.
# 반드시 첫 번째에서 max값으로 시작하는 게 답은 아닌듯?

# def solution(land):
#     result = []
#     for k in range(4): # 열의 갯수는 무조건 4개라고 함.
#         temp = land[0][k]
#         idx = land[0].index(temp)
#
#         for x in range(1, len(land)):
#             while land[x].index(max(land[x])) == idx:
#                 land[x][idx] = 0
#             temp += max(land[x])
#             idx = land[x].index(max(land[x]))
#         result.append(temp)
#     return max(result)

# 위 코드도 모조리 실패.
# 선택할 수 있는 것 중에 최대값만 선택하는 게 답이 아닌가?




























