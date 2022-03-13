
t = int(input())

for _ in range(t):
    n = int(input())
    values = []
    for _ in range(n):
        values.append(list(map(int, input().split())))

    first = 0
    values.sort(key=lambda x:(x[0], x[1])) # 첫 번째 값으로 오름차순
    print(values)
    first_min_value = values[0]
    for i in range(1, len(values)):
        if first_min_value[0] < values[i][0]:
            first += 1

    second = 0
    values.sort(key=lambda x:(x[1], x[0])) # 두 번째 값으로 오름차순
    print(values)
    second_min_value = values[0]
    for j in range(1, len(values)):
        if second_min_value[1] < values[j][1]:
            second += 1
    print(first, second)


???


