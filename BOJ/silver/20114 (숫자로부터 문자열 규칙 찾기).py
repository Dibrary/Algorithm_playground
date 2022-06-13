
n, h, w = map(int, input().split())

strings = []

for _ in range(h):
    strings.append(list(input()))

length = len(strings[0])

tmp = [[] for _ in range(h)]

for i in range(len(strings)):
    for j in range(0, len(strings[0]), length//n):
        tmp[i].append(strings[i][j:j+w])
# 여기서 담은 tmp를 세로로 합쳐야 한다. (set으로 합치면 더 좋음)

results = []

for i in range(len(tmp[0])):
    values = []
    for j in range(len(tmp)):
        values += tmp[j][i]
    results.append(list(values))

answer = ""

for i in results:
    if set(i) == {"?"}:
        answer += "?"
    else:
        for j in i:
            if j != "?":
                answer += j
                break

print(answer)






