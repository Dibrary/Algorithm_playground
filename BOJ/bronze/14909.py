
arr = (1 for x in list(map(int, input().split())) if x >0)

result = 0
for i in arr:
    if i == 1:
        result += 1
print(result)
