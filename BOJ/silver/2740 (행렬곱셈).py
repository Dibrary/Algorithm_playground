
n, m = map(int, input().split())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

n, m = map(int, input().split())
b = []
for _ in range(n):
    b.append(list(map(int, input().split())))

result = []

result = []
for idx, k in enumerate(a):
    tmp = []
    for m in range(len(b[0])):
        temp = 0
        for s in range(len(b)):
            temp += (a[idx][s]*b[s][m])
        tmp.append(temp)
    result.append(tmp)

for r in result:
    print(" ".join(map(str, r)))


# for i in range(len(a)):
#     tmp = []
#     for k in a[i]:
#         temp = 0
#         for j in b:
#             temp += j[i]*k
#         tmp.append(temp)
#     result.append(tmp)
# print(result)




## 다른 사람 코드 ##

import sys

read = sys.stdin.readline

n, m = map(int, read().split())
A = []
B = []

for _ in range(n):
    A.append(list(map(int, read().split())))

m, k = map(int, read().split())
C = [[0 for _ in range(k)] for _ in range(n)]

for _ in range(m):
    B.append(list(map(int, read().split())))

for i in range(n):
    for j in range(k):
        for r in range(m):
            C[i][j] += A[i][r] * B[r][j]

for i in range(n):
    for j in range(k):
        print(C[i][j], end=" ")
    print()

