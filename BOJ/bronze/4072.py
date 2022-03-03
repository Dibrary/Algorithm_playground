
while True:
    n = input().split()
    if n[0] == "#":
        break
    result = []
    for i in n:
        result.append(i[::-1])
    print(" ".join(map(str, result)))



