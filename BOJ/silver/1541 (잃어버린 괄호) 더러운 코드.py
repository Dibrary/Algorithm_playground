
# s = input()
# value = []
# start = 0
# for i in range(0, len(s)):
#     if s[i].isdigit() == False:
#         value.append(s[start:i])
#         start = i
#     elif i == len(s)-1:
#         value.append(s[start:])
# print(value)

'''
+-만 있는 상태에서, 식의 값을 최소로 하려면 -가 최대한 많아지게, 즉, - 뒤에 +는 모조리 묶어버려야 한다.
대신, -뒤에 -가 또 올 경우 바로 그 앞까지만 묶어서 -값이 늘어나게 해야 함.
'''

string = input()

value = []
start_idx = 0

for idx, i in enumerate(string):
    if i.isdigit() == False:
        value.append(int(string[start_idx:idx]))
        start_idx = idx+1
        value.append(i)
value.append(int(string[start_idx:]))
# 입력을 숫자와 operator로 나누는 코드

minus_idx = [] # minus 인덱스만 모음.
for idx, i in enumerate(value):
    if i == "-":
        minus_idx.append(idx)

minus_value_sum = 0 # 최초 마이너스 시작부터 마이너스의 총 합
if minus_idx != []:
    for i in range(len(minus_idx)):
        if i == len(minus_idx)-1: # 맨 끝이라면,
            for k in value[minus_idx[i]+1:]:
                if type(k) == int:
                    minus_value_sum += k
        else:
            for k in value[minus_idx[i]+1:minus_idx[i+1]]:
                if type(k) == int:
                    minus_value_sum += k
    total = 0
    for k in value[:minus_idx[0]]:
        if type(k) == int:
            total += k
else:
    total = 0
    for k in value:
        if type(k) == int:
            total += k

print(total-minus_value_sum)


## 다른 사람 코드 ##

import sys
input = sys.stdin.readline
info = input().split('-')
rst = sum(list(map(int, info[0].split('+'))))
if len(info) != 1:
    for i in range(1, len(info)):
        rst -= sum(list(map(int, info[i].split('+'))))
print(rst)




n = input().split('-')
num = []

for i in n:
    cnt = 0
    s = i.split('+')
    for j in s:
        cnt += int(j)
    num.append(cnt)

temp = num[0]   # 식의 첫 번째

for i in range(1, len(num)):
    temp -= num[i]

print(temp)




from sys import stdin
f = stdin.readline().rstrip().split('-')
s = [sum([int(j) for j in i.split('+')]) for i in f]
print(s[0] - sum(s[1:]))
