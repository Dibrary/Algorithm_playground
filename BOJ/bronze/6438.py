
n = int(input())

for _ in range(n):
    string = input().split() # 들어오면 list로 들어옴
    result = []
    for i in string:
        result.append(i[::-1])
    print(" ".join(map(str, result[::-1])))



