
n = int(input())
table = dict()

for _ in range(n):
    value = input()
    if value not in table:
        table[value] = 1
    else:
        table[value] += 1
print(table)

# 문제 이해 못함.;

