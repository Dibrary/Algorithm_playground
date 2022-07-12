
tmp = []
for i in range(1, 110):
    tmp.append(i**2)

m = int(input())
n = int(input())

result = []
min_value = 0

for i in tmp:
    if m <= i <= n:
        if min_value == 0:
            min_value = i
        result.append(i)

if result == []:
    print(-1)
else:
    print(sum(result))
    print(min_value)
