# from itertools import combinations
#
# S = input()
#
# table = set()
#
# for i in range(1,len(S)+1):
#     for k in combinations(list(S), i):
#         if k not in table:
#             table.add(k)
#
# print(len(table))

# 위 방법은 갯수 못셈


# S = input()
#
# table = set()
#
# for i in range(1, len(S)+1):
#     for j in range(0, len(S)-i+1):
#         if S[j:j+i] not in table:
#             table.add(S[j:j+i])
# print(len(table))

# 위 코드 틀림



