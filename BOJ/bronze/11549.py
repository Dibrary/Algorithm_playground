t = int(input())

for _ in range(t):
    n, p = input().split()
    value = input().split()
    if p == "C":
        result = ""
        for i in value:
            result += str(ord(i)-64)+" "
        print(result[:-1])
    else:
        result = ""
        for i in value:
            result += chr(int(i)+64) +" "
        print(result[:-1])






