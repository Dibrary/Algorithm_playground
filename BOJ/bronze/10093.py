
a, b = map(int, input().split())

result = [x for x in range(a+1, b)]

print(len(result))

print(" ".join(map(str, result)))

# 위 방식으로 계산 틀림

