n = int(input())
k = int(input())

result = n
for i in range(k):
    n = str(n)+"0"
    result += int(n)
print(result)