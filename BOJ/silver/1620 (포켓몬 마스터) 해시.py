
# from collections import defaultdict
#
# no_dict = defaultdict(str)
# name_dict = defaultdict(int)
#
# n, m = map(int, input().split())
# for x in range(n):
#     name = input()
#     no_dict[x] = name
#     name_dict[name] = x
#
# for _ in range(m):
#     value = input()
#     if value.isdigit():
#         print(no_dict[int(value)])
#     else:
#         print(name_dict[value])

# 16%에서 틀림

# import sys
# from collections import defaultdict
# input = sys.stdin.readline
#
# no_dict = defaultdict(str)
# name_dict = defaultdict(int)
#
# n, m = map(int, input().split())
# for x in range(1, n+1): # 인덱스 수정해 줌
#     name = input()
#     no_dict[x] = name
#     name_dict[name] = x
#
# for _ in range(m):
#     value = input()
#     if value.isdigit():
#         print(no_dict[int(value)])
#     else:
#         print(name_dict[value])

# 이것도 16%에서 틀림

import sys
from collections import defaultdict
input = sys.stdin.readline

no_dict = defaultdict(str)
name_dict = defaultdict(int)

n, m = map(int, input().split())
for x in range(1, n+1): # 인덱스 수정해 줌
    name = input().rstrip()
    no_dict[x] = name
    name_dict[name] = x

for _ in range(m):
    value = input().rstrip() # 이거 때문에 16%에서 계속 틀린것.
    if value.isdigit():
        print(no_dict[int(value)])
    else:
        print(name_dict[value])




## 다른 사람 코드 ##

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

dict = {}

for i in range(1, n + 1):
    a = input().rstrip()
    dict[i] = a
    dict[a] = i

for i in range(m):
    quest = input().rstrip()
    if quest.isdigit():
        print(dict[int(quest)])
    else:
        print(dict[quest])








import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dictionary = dict()

for i in range(1, N+1):
    name = input().rstrip()
    dictionary[name] = i
    dictionary[i] = name

for _ in range(M):
    query = input().rstrip()
    if query.isdigit():
        print(dictionary[int(query)])
    else:
        print (dictionary[query])


