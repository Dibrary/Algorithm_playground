
import sys
sys.setrecursionlimit(10**5)

X = list(input())
Y = list(input())

m = len(X)
n = len(Y)

# def LCS(X, Y, m, n):
#     if m == 0 or n == 0:
#         return 0
#     elif X[m-1] == Y[n-1]:
#         return 1 + LCS(X, Y, m-1, n-1)
#     else:
#         return max(LCS(X, Y, m-1, n), LCS(X, Y, m, n-1))
#
# print(LCS(X, Y, m, n))

# 위 코드는 시간초과 걸린다.

L = [[None]*(n+1) for _ in range(m+1)]

for i in range(m+1):
    for j in range(n+1):
        if i == 0 or j == 0:
            L[i][j] = 0
        elif X[i-1] == Y[j-1]:
            L[i][j] = L[i-1][j-1]+1
        else:
            L[i][j] = max(L[i-1][j], L[i][j-1])
print(L[m][n])

# DP로 풀면 시간초과 안 걸린다.


## 다른 사람 코드 ##



