
start, end = map(int, input().split())

table = [0 for x in range(0, 10)]

for i in range(start, end+1):
    tmp = str(i)
    for k in tmp:
        table[int(k)] += 1
print(" ".join(map(str, table))) # 출력 형식 이렇게 해 줘야 맞음.

