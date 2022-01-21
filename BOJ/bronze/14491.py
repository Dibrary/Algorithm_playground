n = int(input())

result = ""
while True:
    if n >= 9:
        result += str(n%9)
        n = n//9
    else:
        result += str(n)
        break
print(result[::-1])

#진법 변환 하는 방법