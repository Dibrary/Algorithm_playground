t = int(input())

for _ in range(t):
    tmp = list(map(int, input().split()))
    tmp = tmp[1:]
    odd = 0
    even = 0
    for i in tmp:
        if i%2 == 0:
            even += i
        else:
            odd += i

    if odd > even:
        print("ODD")
    elif odd < even:
        print("EVEN")
    elif odd == even:
        print("TIE")

