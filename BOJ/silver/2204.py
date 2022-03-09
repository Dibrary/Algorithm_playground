
while True:
    n = int(input())
    if n == 0:
        break

    table = dict()
    for i in range(n):
        s = input()
        table[s.lower()] = s

    tmp = list(table.keys())
    tmp.sort()
    print(table[tmp[0]])




