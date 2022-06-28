# def dailyTemperatures(temperatures):
#     result = []
#     for i in range(0, len(temperatures) - 1):
#         value = temperatures[i]
#         cnt = 0
#         for j in range(i + 1, len(temperatures)):
#             if temperatures[j] >= value: # 여기 부등호 때문에 에러 남.
#                 cnt += 1
#                 break
#             elif j == len(temperatures) - 1 and temperatures[j] < value:
#                 cnt = 0
#             else:
#                 cnt += 1
#         result.append(cnt)
#     result.append(0)
#     return result
#
# def dailyTemperatures(temperatures):
#     result = []
#     for i in range(0, len(temperatures) - 1):
#         value = temperatures[i]
#         cnt = 0
#         for j in range(i + 1, len(temperatures)):
#             if temperatures[j] > value:
#                 cnt += 1
#                 break
#             elif j == len(temperatures) - 1 and temperatures[j] <= value: # 여기 부등호 추가 해야 됨.
#                 cnt = 0
#             else:
#                 cnt += 1
#         result.append(cnt)
#     result.append(0)
#     return result

# [34,80,80,80,34,80,80,80,34,34] 에러
# 그 다음에러는 시간초과 에러;; 데이터 갯수 10000개;;




