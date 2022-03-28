
n = int(input())
for _ in range(n):
    a, b, c = map(int, input().split())
    angle = a+b+c
    if angle == 180:
        print(f'{a} {b} {c} Seems OK')
    else:
        print(f'{a} {b} {c} Check')
