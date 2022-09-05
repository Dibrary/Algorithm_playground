
'''
문제에서 몇 개의 쌍이 비슷하다는 얘기는, 이미 쌍이 같은게 확인 된 것은 세지 않아야 한다는 것인가?
'''
# n = int(input())
#
# strings = []
# for i in range(n):
#     strings.append(input())
#
# cnt = 0
# for i in range(0, len(strings)-1):
#     for j in range(i+1, len(strings)):
#         tmp = dict()
#
#         for k in range(len(strings[0])):
#             if strings[i][k] != strings[j][k]:
#                 if (strings[i][k], strings[j][k]) not in tmp:
#                     tmp[(strings[i][k], strings[j][k])] = 1
#                 else:
#                     tmp[(strings[i][k], strings[j][k])] += 1
#         if len(tmp) <= 2:
#             cnt += 1
# print(cnt)

# 위 코드는 안맞음.

# n = int(input())
#
# cnt = 0
# for i in range(n):
#     if i == 0:
#         string = input()
#     else:
#         compare = input()
#         tmp = dict()
#
#         for k in range(len(string)):
#             if string[k] != compare[k]:
#                 if (string[k], compare[k]) not in tmp:
#                     tmp[(string[k], compare[k])] = 1
#                 else:
#                     tmp[(string[k], compare[k])] += 1
#         if len(tmp) <= 2:
#             cnt += 1
# print(cnt)

# 위 코드도 안 맞음


from collections import defaultdict

n = int(input())

strings = []
for i in range(n):
    strings.append(input())

cnt = 0
table = set()

for i in range(0, len(strings)-1):
    for j in range(i+1, len(strings)):
        if strings[j] not in table:
            tmp = dict()
            for a, b in zip(strings[i], strings[j]):
                if a != b:
                    if (a, b) not in tmp:
                        tmp[(a, b)] = 1
                    else:
                        tmp[(a, b)] += 1

            if len(tmp) <= 2:
                cnt += 1
                table.add(strings[i])
                table.add(strings[j])
            print(table) # 이렇게도 안 된다.
print(cnt)










## 다른 사람 코드 ##

import sys

n = int(sys.stdin.readline())
temp = [[] for _ in range(101)]
dic = [{} for i in range(101)]
cnt = 0

# 반복문을 통해 단어를 확인
for i in range(n):
    num = 0
    m = str(sys.stdin.readline()).rstrip('\n')

    # 반복문을 통해 알파벳을 확인하고
    # 그 알파벳을 수와 같이 딕셔너리형으로 추가한다.
    for j in m:
        if j not in dic[i]:
            dic[i][j] = str(num)
            num += 1

        # 현재 확인한 알파벳을 temp에 추가한다.
        temp[i] += dic[i][j]

# 반복문을 통해 같은 단어라면 카운트한다.
for i in range(n):
    for j in range(i + 1, n):
        if temp[i] == temp[j]:
            cnt += 1

print(cnt)










import sys
from collections import defaultdict, Counter

def get_pattern(s):
    i = 0
    d = {}
    pattern = []
    for c in s:
        if c not in d:
            d[c] = i
            i += 1
        pattern.append(d[c])

    return tuple(pattern)

N = int(sys.stdin.readline().rstrip())

dic = defaultdict(int)
words = [sys.stdin.readline().rstrip() for _ in range(N)]
patterns = [get_pattern(word) for word in words]

print(sum(map(lambda x: x * (x - 1) // 2, Counter(patterns).values())))












import sys
from collections import defaultdict
input = sys.stdin.readline

def solve(a, b):
    d = defaultdict(str)
    for i in range(len(a)):
        if d[a[i]]:
            if d[a[i]] != b[i]:
                return 0
        else:
            if b[i] in list(d.values()):
                return 0
            d[a[i]] = b[i]
    return 1

n = int(input())
a = [list(input().strip()) for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(i+1, n):
        if solve(a[i], a[j]):
            ans += 1
print(ans)












n = int(input())
lists = [input() for _ in range(n)]
cnt = 0
for i in range(0, n - 1):
    for j in range(i + 1, n):
        s1 = lists[i]
        s2 = lists[j]
        flag = True
        if len(s1) == len(s2):
            visit1 = [0] * 26
            visit2 = [0] * 26
            for k in range(len(s1)):
                idx1 = ord(s1[k]) - ord('a')
                idx2 = ord(s2[k]) - ord('a')

                if visit1[idx1] == 0 and visit2[idx2] == 0:
                    visit1[idx1] = s2[k]
                    visit2[idx2] = s1[k]
                elif visit1[idx1] != s2[k]:
                    flag = False
                    break
        if flag:
            cnt += 1
print(cnt)











import sys

n = int(sys.stdin.readline())
word_to_num_list = []
for i in range(n):
    word = sys.stdin.readline()
    dic = {}
    num = 0
    word_to_num = ""
    for s in word:
        if s in dic.keys():
            word_to_num+= dic[s]
        else:
            dic[s] = str(num)
            word_to_num += dic[s]
            num+=1
    word_to_num_list.append(word_to_num)

cnt = 0
for i in range(len(word_to_num_list)):
    cnt += word_to_num_list[i+1:].count(word_to_num_list[i])
print(cnt)



