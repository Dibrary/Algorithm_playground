
while True:
    n = int(input())
    if n == 0:
        break

    datas = dict()

    for i in range(n):
        name, height = input().split()
        datas[(name, i)] = float(height)

    max_height = max(datas.values())
    temp = []
    for i in datas:
        if datas[i] == max_height:
            temp.append(i)

    # 위 코드     temp = [x for x in datas if datas[x] == max_height]
    # 이렇게 한 줄로 처리 가능.

    temp.sort(key=lambda x:x[1])

    results = []
    for data in temp:
        results.append(data[0])

    print(" ".join(map(str, results)))




