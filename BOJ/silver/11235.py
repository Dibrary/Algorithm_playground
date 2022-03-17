
n = int(input())
temp = dict()

for _ in range(n):
    name = input()
    if name not in temp:
        temp[name] = 1
    else:
        temp[name] += 1

max_count = max(temp.values())

result = []
for i in temp:
    if temp[i] == max_count:
        result.append(i)
result.sort()

for k in result:
    print(k)


