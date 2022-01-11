n = int(input())

for i in range(n):
    score = input()

    cnt = 0
    result = 0
    for idx, i in enumerate(score):
        if i == "O" and idx == 0:
            cnt += 1
            result += cnt
        elif i == "O":
            cnt += 1
            result += cnt
        elif i == "X":
            cnt = 0
    print(result)


