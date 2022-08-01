

# n, m = list(map(int, input().split()))
# maps = []
# for _ in range(n):
#     row = list(map(int, input().split()))
#     maps.append(row)
#
# chickens = []
# houses = []
#
# for i in range(0, len(maps)):
#     for j in range(0, len(maps[0])):
#         if maps[i][j] == 2:
#             chickens.append((i,j))
#         elif maps[i][j] == 1:
#             houses.append((i,j))
# print(chickens, houses)
#
# min_distance = 999999999
# for i in chickens:
#     tmp = 0
#     for j in houses:
#         tmp += (abs((j[0]+1)-(i[0]+1)) + abs((j[1]+1)-(i[1]+1)))
#     print(tmp, "tmp")
#     if tmp <= min_distance:
#         min_distance = tmp
# print(min_distance)









## 책 풀이 ##

from itertools import combinations

n, m = map(int, input().split())
chicken, house = [], []

for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r, c))
        elif data[c] == 2:
            chicken.append((r, c))

candidates = list(combinations(chicken, m))

def get_sum(candidate):
    result = 0

    for hx, hy in house:
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx-cx) + abs(hy-cy))
        result += temp
    return result

result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))

print(result)



