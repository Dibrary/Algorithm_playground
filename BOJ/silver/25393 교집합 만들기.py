
'''
문제 이해가 안 되네, 예제에서 4 6은, 결국 3개 모두 가능할텐데 출력이 2다.

'''
# n = int(input())
# tmp = dict()
#
# for _ in range(n):
#     l, r = map(int, input().split())
#
#     for k in range(l, r+1):
#         if k not in tmp:
#             tmp[k] = 1
#         else:
#             tmp[k] += 1
# print(tmp)
#
# q = int(input())
# for _ in range(q):
#     result = 1e9
#     l, r = map(int, input().split())
#
#     for k in range(l, r+1):
#         if result >= tmp[k]:
#             result = tmp[k]
#     if result == 1e9:
#         print(-1)
#     else:
#         print(result)





# from collections import defaultdict
#
# n = int(input())
# total = []
# start = defaultdict(int)
# end = defaultdict(int)
#
# for _ in range(n):
#     l, r = map(int, input().split())
#     total.append((l, r))
#     start[l] += 1
#     end[r] += 1
#
# q = int(input())
# for _ in range(q):
#     a, b = map(int, input().split())
#     if start[a] == 0 and end[b] == 0:
#         print(-1)
#     elif start[a] != 0 and end[b] != 0:
#         if (a, b) in total:
#             print(1)
#         else:
#             print(2)

# 근데 위 코드로 해버리면 교집합이 불완전한(안 되는) 경우도 OK로 취급되어버림;




# from collections import defaultdict
#
# n = int(input())
# total = []
# start = defaultdict(list)
# end = defaultdict(list)
#
# for _ in range(n):
#     l, r = map(int, input().split())
#     total.append((l, r))
#     start[l].append(r)
#     end[r].append(l)
#
# q = int(input())
# for _ in range(q):
#     a, b = map(int, input().split())
#     if start[a] == [] and end[b] == []:
#         print(-1)
#     elif start[a] != [] and end[b] != []:
#         if sorted(start[a], key=lambda x:-x)[0] > b and sorted(end[b], key=lambda x:x)[0] < a:
#             print(2)
#         elif b in start[a] or a in end[b]:
#             print(1)
#         else:
#             print(-1)

# 위 코드 3%에서 시간초과 걸린다.
# pypy로 변경하면 7%에서 틀린다.









