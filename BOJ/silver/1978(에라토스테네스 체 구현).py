sheve = [x for x in range(1100)]
sheve[1] = 0

for s in sheve[2:]:
    for k in range(2, 1100):
        if s * k < len(sheve):
            sheve[s * k] = 0

n = int(input())
values = list(map(int, input().split()))

cnt = 0
for i in values:
    if i in sheve:
        cnt += 1
print(cnt)