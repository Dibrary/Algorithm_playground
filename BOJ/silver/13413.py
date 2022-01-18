# import copy
#
# n = int(input())
#
# for _ in range(n):
#     length = int(input())
#     first = list(input())
#     standard = list(input())
#
#     cnt = 0
#     if len(set(first)) == 1:
#         for i in range(0, len(first)):
#             if first[i] != standard[i]:
#                 cnt += 1
#         print(cnt)
#     else:
#         tmp = copy.deepcopy(first)
#         for i in range(0, len(first) - 2):
#             if first[i:i + 2][::-1] == standard[i:i + 2]:
#                 first[i:i + 2] = first[i:i + 2][::-1]
#                 print(first)
#                 cnt += 1
#             else:
#                 break
#         if first == standard:
#             print(cnt)
#         else:
#             cnt1, cnt2 = 0, 0
#             for i in range(0, len(first)):
#                 if first[i] != standard[i]:
#                     cnt1 += 1
#                 if i != len(first) - 2:
#                     if first[i:i + 2][::-1] == standard[i:i + 2]:
#                         print(first[i:i + 2][::-1], standard[i:i + 2])
#                         cnt2 += 1
#             print(cnt1, cnt2, cnt2 - cnt1)

'''
초반에 위 처럼 하려다가 코드가 너무 난잡해짐.
떠오른 생각은 교환은 한 번에 2개를 바꾸고, 변환은 한 번에 1개를 바꾼다는 것.
최소로 하려면 교환을 많이 해야 한다.

'''

n = int(input())

for _ in range(n):
    t = int(input())
    first = list(input())
    standard = list(input())

    cnt = 0
    for i in range(0, len(first) - 1):
        if first[i:i + 2][::-1] == standard[i:i + 2]:
            first[i:i + 2] = first[i:i + 2][::-1]
            cnt += 1
    for k in range(0, len(first)):
        if first[k] != standard[k]:
            cnt += 1

    print(cnt)
# 근데 틀렸다고 한다.





