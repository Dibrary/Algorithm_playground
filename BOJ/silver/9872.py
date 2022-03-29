
n = int(input())
table = dict()

for _ in range(n):
    cows = list(input().split())
    cows.sort()
    cows = tuple(cows)
    if cows not in table:
        table[cows] = 1
    else:
        table[cows] += 1
max_value = max([table[x] for x in table])
print(max_value)

