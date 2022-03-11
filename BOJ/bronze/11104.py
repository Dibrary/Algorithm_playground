
n = int(input())

for _ in range(n):
    result = 0
    value = input()
    value = value[::-1]
    for idx, value in enumerate(value):
        result += int(value)*(2**idx)
    print(result)


