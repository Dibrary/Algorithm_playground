n = int(input())

for _ in range(n):
    arr = list(input().split())

    result = float(arr[0])
    for i in range(1, len(arr)):
        if arr[i] == "@":
            result *= 3
        elif arr[i] == "%":
            result += 5
        elif arr[i] == "#":
            result -= 7
    print("{:.2f}".format(result)) # 여기서 출력 방법이 중요하다.
