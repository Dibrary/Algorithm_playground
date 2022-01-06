
n = int(input())
arr = list(set(map(int, input().split())))
arr.sort()
result = ""
for i in arr:
    result += str(i) + " "
print("%s"%(result[:-1]))
