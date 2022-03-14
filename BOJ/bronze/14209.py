
n = int(input())

def calc(value):
    tmp = 0
    if "A" in value:        tmp += value.count("A") * 4
    if "K" in value:        tmp += value.count("K") * 3
    if "Q" in value:        tmp += value.count("Q") * 2
    if "J" in value:        tmp += value.count("J") * 1
    return tmp

result = 0
for _ in range(n):
    value = input()
    result += calc(value)
print(result)