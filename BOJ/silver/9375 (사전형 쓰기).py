
'''
의상 이름, 의상 종류로 입력이 주어진다.

이 문제의 해법은
의상 종류에 이름이 몇 개 있는지를 알면 된다. (모든 경우의 수를 고려하기 위해서)
의상 종류별로 (이름+1) 을 모두 곱한 후 마지막에 -1만 해 주면 됨. (아무것도 선택하지 않는 경우)
'''

n = int(input())

for _ in range(n):
    m = int(input())

    tmp = dict()
    for _ in range(m):
        a, b = input().split()
        if b not in tmp:
            tmp[b] = [a]
        else:
            tmp[b].append(a)

    result = 1
    for keys in tmp:
        result *= len(tmp[keys])+1
    print(result-1)




### 책 풀이 ###
testcase= int(input())

for i in range(testcase):
    map = {}
    answer = 1
    n = int(input())
    for j in range(n):
        a, b = input().split()
        if not b in map:
            map[b] = 1
        else:
            map[b] += 1
    for k in map.keys():
        answer = answer * (map[k]+1)
    print(answer-1)



## 다른 사람 코드 ##

import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    dic = {}
    answer=1
    for _ in range(n):
        name, cat = map(str, sys.stdin.readline().strip().split())
        if cat in dic.keys():
            dic[cat].append(name)
        else:
            dic[cat] = [name]
    for category in dic.keys():
        answer *= (len(dic[category])+1)
    print(answer-1)