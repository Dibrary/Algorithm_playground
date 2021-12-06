n = int(input())

weights = []
for i in range(n):
    weights.append(tuple(map(int, input().split())))

result = ""
for k in range(0, len(weights)):
    tmp_weights = weights[:k] + weights[k+1:]
    # print(tmp_weights, weights[k]) # 제출할 때 이런 중간 출력이 들어가면 '출력 초과'라고 나온다.
    value = 1
    for i in tmp_weights:
        if weights[k][0] < i[0] and weights[k][1] < i[1]:
            value += 1
    result += str(value)+" "

print(result[:-1])