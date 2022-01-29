
t = int(input())
arr = input()

result = 0
for k in arr:
    result += (ord(k)-ord("A")+1)
print(result)



