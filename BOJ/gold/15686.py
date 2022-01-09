
n, m = list(map(int, input().split()))
maps = []
for _ in range(n):
    row = list(map(int, input().split()))
    maps.append(row)

chickens = []
houses = []

for i in range(0, len(maps)):
    for j in range(0, len(maps[0])):
        if maps[i][j] == 2:
            chickens.append((i,j))
        elif maps[i][j] == 1:
            houses.append((i,j))
print(chickens, houses)

min_distance = 999999999
for i in chickens:
    tmp = 0
    for j in houses:
        tmp += (abs((j[0]+1)-(i[0]+1)) + abs((j[1]+1)-(i[1]+1)))
    print(tmp, "tmp")
    if tmp <= min_distance:
        min_distance = tmp
print(min_distance)




