
n, m = map(int, input().split())

for _ in range(n):
    value = input()
    reverse = value[::-1]
    result = ""
    for i in range(0, len(value)):
        if value[i] != "." or reverse[i] != ".":
            if value[i] != ".":
                result += value[i]
            else:
                result += reverse[i]
        elif value[i] == "." and reverse[i] == ".":
            result += "."
    print(result)


