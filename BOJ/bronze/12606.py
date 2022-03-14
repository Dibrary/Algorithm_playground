
n = int(input())

for i in range(1, n+1):
    string = list(input().split())

    result = ""

    for s in string[::-1]:
        result += s + " "
    print(f'Case #{i}: {result[:-1]}')
