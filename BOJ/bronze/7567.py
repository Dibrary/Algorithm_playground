

target = input()
result = 10

for i in range(1, len(target)):
    if target[i] == target[i-1]:
        result += 5
    else:
        result += 10
print(result)