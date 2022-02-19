n = int(input())

a_tot, b_tot, c_tot = 0,0,0
for _ in range(n):
    a, b, c = map(int, input().split())
    a_tot += a
    b_tot += b
    c_tot += c

    if a_tot < 30 or b_tot < 30 or c_tot < 30:
        print("NO")
        continue
    else:
        min_value = min([a_tot, b_tot, c_tot])
        print(min_value)
        a_tot -= min_value
        b_tot -= min_value
        c_tot -= min_value