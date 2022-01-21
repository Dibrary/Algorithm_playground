n = int(input())
for _ in range(n):
    value = bin(int(input()))[2:][::-1]
    result = []
    for i in range(0, len(value)):
        if value[i] == "1":
            result.append(i)
    print(" ".join(map(str, result)))