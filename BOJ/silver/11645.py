
t = int(input())

for _ in range(t):
    n = int(input())
    tmp = dict()
    for _ in range(n):
        city = input()
        if city not in tmp:
            tmp[city] = 1
    print(len(tmp))