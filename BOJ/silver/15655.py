from itertools import combinations

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

result = []
for j in combinations(arr, m):
    result.append(j)
for k in result:
    print(" ".join(map(str, k)))