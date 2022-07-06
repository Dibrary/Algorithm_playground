
'''
대놓고 플로이드 워셜 문제다.

모든 도시 쌍에 대해서 가는 비용의 최솟값을 구하라고 함.
'''

# import sys
#
# n = int(input()) # 도시(노드) 갯수
# m = int(input()) # 버스(간선) 갯수
#
# INF = sys.maxsize
#
# graph = [[INF]*(n+1) for _ in range(n+1)]
#
# for a  in range(1, n+1):
#     for b in range(1, n+1):
#         if a == b:
#             graph[a][b] = 0
#
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a][b] = c
#
# for k in range(1, n+1):
#     for a in range(1, n+1):
#         for b in range(1, n+1):
#             graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
#
# print(graph[1:]) # 원하는 형태로 나오지 않음. 일부 몇 줄이 다르다.




## 다른 사람 코드 ##
n = int(input())
m = int(input())
inf = 100000000
s = [[inf] * n for i in range(n)]

for i in range(m):
    a, b, c = map(int, input().split())
    if s[a - 1][b - 1] > c:
        s[a - 1][b - 1] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i != j and s[i][j] > s[i][k] + s[k][j]:
                s[i][j] = s[i][k] + s[k][j]

for a  in range(n):
    for b in range(n):
        if a == b:
            s[a][b] = 0


for k in s:
    print(" ".join(map(str, k)))

# 위 코드 98%에서 틀림









