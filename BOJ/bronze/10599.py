
while True:
    a, b, c, d  = map(int, input().split())
    if a == 0 and b == 0 and c == 0 and d == 0:
        break

    start_max = max(a, b)
    start_min = min(a, b)
    end_max = max(c, d)
    end_min = min(c, d)
    print(f'{abs(end_min-start_max)} {abs(end_max-start_min)}')

