n = int(input())

table = [0, 1]
for i in range(2, 1000001):
    table.append((i**2)+(table[i-1]))

for _ in range(n):
    i = int(input())
    print(table[i])


