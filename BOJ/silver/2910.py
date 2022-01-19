n, c = map(int, input().split())

table = []

arr = list(map(int, input().split()))
for i in arr:
    if (i, arr.count(i)) not in table:
        table.append((i, arr.count(i)))

table.sort(key=lambda x: x[1], reverse=True)

for i in range(0, len(table)):
    for k in range(table[i][1]):
        if i == len(table) - 1 and k == table[i][1] - 1:
            print(table[i][0])
        else:
            print(table[i][0], end=" ")

# 일종의 많이 나온 횟수를 기준으로 정렬