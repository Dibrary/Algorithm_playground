
'''
이 문제의 핵심은 파티에 참석한 사람들을 1개의 집합으로 보고, 각 파티마다 union 연산으로 사람들을 연결하는 것이다.

파티마다 오는 사람의 수가 1 이상 50이하 정수라는 것은 union 연산을 그만큼 중첩해서 많이 해야 한다는 것인가?

'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(a):
    if a == parent[a]:
        return a
    p = find(parent[a])
    parent[a] = p
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    if a > b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
arr = list(map(int, input().split())) # 0이면 0 한개만 있고, 1이면 1 number 이렇게 주어진다.

parent = [k for k in range(n+1)]

for _ in range(m):
    tmp = list(map(int, input().split()))
    if tmp[0] == 1:
        continue
    else:
        for k in range(1, len(tmp)-1):
            for j in range(k+1, len(tmp)):
                union(tmp[k], tmp[j])

# 위 코드에서 나온 parent가 뭘 의미하는지 모르겠음 #








## 다른 사람 코드 ##
n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

def find_parent(x):
    if parent[x] == x:
        return x
    p = find_parent(parent[x])
    parent[x] = p
    return p

def union(x, y):
    x = find_parent(x)
    y = find_parent(y)
    if x != y:
        parent[y] = parent[x]

trueList = list(map(int, input().split()))

#1
for i in range(trueList[0]):
    union(trueList[1], trueList[i + 1])

party = []

#2
for _ in range(m):
    party.append(list(map(int, input().split())))
    party_num = party[-1][0]
    for cur in range(party_num - 1):
        union(party[-1][cur + 1], party[-1][cur + 2])
#3
ans = 0
for i in party:
    for cur in range(i[0]):
        if (len(trueList) > 1 and find_parent(i[cur + 1]) == find_parent(true[1])):
            ans += 1
            break

print(m - ans)










import sys
input = sys.stdin.readline

n, m = map(int, input().split())
knowList = set(input().split()[1:])
parties = []

for _ in range(m):
    parties.append(set(input().split()[1:]))

for _ in range(m):
    for party in parties:
        if party & knowList:
            knowList = knowList.union(party)

cnt = 0
for party in parties:
    if party & knowList:
        continue
    cnt += 1

print(cnt)







import sys
input = sys.stdin.readline

cnt_party = int(input().rstrip().split()[1])
witness_set = set(input().rstrip().split()[1:])

party_list = []
possible_list = []

for _ in range(cnt_party):
    party_list.append(set(input().rstrip().split()[1:]))
    possible_list.append(1)

for _ in range(cnt_party):
    for i, party in enumerate(party_list):
        if witness_set.intersection(party):
            possible_list[i] = 0
            witness_set = witness_set.union(party)

print(sum(possible_list))







import sys
input = sys.stdin.readline

# N : 사람의 수 ,  M : 파티의 수
N, M = map(int,input().split())
know_truth = set(list(map(int,input().split()))[1:])


parties = []
for _ in range(M):
    party_member = list(map(int,input().split()))[1:]
    parties.append(party_member)

truth_party = [0] * M


for _ in range(M): # 파티 수만큼 반복해라.
    for idx, party in enumerate(parties):
        if know_truth.intersection(set(party)):
            # 여기는 이제 진실을 아는 사람들이 있는 파티니까...표시해야겠지
            truth_party[idx] = 1
            know_truth = know_truth.union(set(party))

print(truth_party.count(0))