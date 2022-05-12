
# import sys, copy
# input = sys.stdin.readline
#
# a = list(input())
# b = list(input())
#
# cnt = 0
# b_copy = copy.deepcopy(b)
# for i in a:
#     if i in b_copy:
#         b_copy.remove(i)
#     else:
#         cnt += 1
# a_copy = copy.deepcopy(a)
# for j in b:
#     if j in a_copy:
#         continue
#     else:
#         cnt += 1
# print("%d"%(cnt))

# 틀림

# a = input()
# b = input() # 항상 입력의 길이가 같지 않을 수 있다.
#
# cnt = 0
#
# for i in a:
#     if i not in b:
#         cnt += 1
# for j in b:
#     if j not in a:
#         cnt += 1
# print(cnt)

# 아주 그냥 곧바로 틀림

import copy

a = input()
b = input()

cnt = 0
b_copy = list(copy.deepcopy(b))
for i in a:
    if i in b_copy:
        b_copy.remove(i) # remove 하면 같은 게 여러개여도 한 개만 지워지는 것에 착안.

cnt += len(b_copy)

a_copy = list(copy.deepcopy(a))

for j in b:
    if j in a_copy:
        a_copy.remove(j)

cnt += len(a_copy)

print(cnt)

