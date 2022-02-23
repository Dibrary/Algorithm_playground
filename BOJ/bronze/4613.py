# 띄어쓰기 ord 하면 32 나온다.

while True:
    n = input()
    if n == "#": break

    string = list(n)

    result = 0
    for i in range(1, len(string)+1):
        if n[i-1] == " ":
            continue
        else:
            result += (i*(ord(n[i-1])-64))
    print(result)


