import sys
input = sys.stdin.readline

table = dict()
n = int(input())

for _ in range(n):
    name, state = input().split()
    if state == "enter":
        table[name] = 1
    elif state == "leave":
        table[name] = 0

result = []
for i in table:
    if table[i] == 1:
        result.append(i)

result.sort(reverse=True)

for k in result:
    print(k)

# 아래 코드 시간초과 걸림. 그래서 위 코드로 수정함. (dict를 사용하게)

import sys
input = sys.stdin.readline

result = []
n = int(input())

tmp = []
for _ in range(n):
    name, state = input().split()
    if state == "enter":
        result.append(name)
    elif state == "leave":
        result.remove(name)

result.sort(reverse=True)

for k in result:
    print(k)