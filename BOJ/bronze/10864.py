
# n, m = map(int, input().split())
#
# table = dict()
#
# for _ in range(m):
#     a, b = map(int, input().split())
#     if a not in table:
#         table[a] = 1
#     else:
#         table[a] += 1
#
#     if b not in table:
#         table[b] = 1
#     else:
#         table[b] += 1
#
# for k in table.values():
#     print(k)
# 틀렸다.;'

# n, m = map(int, input().split())
#
# table = dict()
#
# for _ in range(m):
#     a, b = map(int, input().split())
#
#     if a not in table:
#         table[a] = [b]
#     else:
#         table[a].append(b)
#
#     if b not in table:
#         table[b] = [a]
#     else:
#         table[b].append(a)
#
# for k in table.values():
#     print(len(k))

# 틀렸다.;'


n, m = map(int, input().split())
table = [0 for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    table[a] += 1
    table[b] += 1

for k in range(1, len(table)):
    print(table[k])

## 다른 사람 코드 ##

n, m = map(int, input().split())
lis = [[] for _ in range(n)]    # 친구 리스트
for _ in range(m):
    a, b = map(int, input().split())
    if not a in lis[b-1]: lis[b-1].append(a)
    if not b in lis[a-1]: lis[a-1].append(b)
for i in range(n):
    print(len(lis[i]))







N, M = map(int, input().split())
arr = [0] * (N + 1)
for _ in range(M):
    a, b = map(int, input().split())
    arr[a] += 1
    arr[b] += 1

for i in range(1, N + 1):
    print(arr[i])



