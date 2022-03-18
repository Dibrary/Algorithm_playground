
n = int(input())

for _ in range(n):
    value = input()
    tmp = dict()

    for k in value:
        if k != " " and k not in tmp:  tmp[k] = 1
        elif k != " " and k in tmp:    tmp[k] += 1

    max_value = max(tmp.values())
    result = [x for x in tmp if tmp[x] == max_value] # 한 번에 max_value를 값으로 갖는 key만 모은다.

    if len(result) != 1:print("?")
    else:               print(result[0])

