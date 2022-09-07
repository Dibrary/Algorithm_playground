# import sys
# input = sys.stdin.readline
# n, m = map(int, input().split())
# girls = dict()
#
# for _ in range(n):
#     name = input()
#     count = int(input())
#     girls[name] = []
#
#     for _ in range(count):
#         girls[name].append(input())
#
# for _ in range(m):
#     word = input()
#     div = int(input())
#     if div == 0:
#         if word in girls.keys():
#             result = girls[word]
#             result.sort()
#             for k in result:
#                 print(k)
#     else:  # 구분이 1인 경우
#         for k in girls.keys():
#             if word in girls[k]:
#                 print(k)

# 출력 형식이 잘못되었다네?

from collections import defaultdict

n, m = map(int, input().split())
team, member = defaultdict(list), defaultdict()

for _ in range(n):
    name = input()
    number = int(input())
    for _ in range(number):
        girl = input()
        team[name].append(girl)
        member[girl] = name

for _ in range(m):
    string = input()
    no = int(input())
    if no == 1:
        print(member[string])
    else:
        mem = team[string]
        print('\n'.join(sorted(mem)))


## 다른 사람 코드 ##

import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # n은 걸그룹 수, m은 퀴즈 수
team = {}

for _ in range(n):
    name = input().rstrip() # 팀 이름 저장
    team[name] = []
    for _ in range(int(input())): # 멤버 이름 저장
        team[name].append(input().rstrip())
    team[name].sort()

for _ in range(m): # 1: 팀 출력, #0: 멤버 출력
    quiz = input().rstrip()
    if int(input()) == 1:
        print(''.join([k for k, v in team.items() if quiz in v]))
    else:
        print('\n'.join(*[v for k, v in team.items() if quiz in k]))









n, m = map(int,input().split())
l = {}
for i in range(n):
    s = input()
    for i in range(int(input())):
        a = input()
        if s not in l:
            l[s] = [a]
        else:
            l[s].append(a)
            l[a] = [s]
for i in range(m):
    c = input()
    d = int(input())
    for j in sorted(l[c]):
        print(j)

