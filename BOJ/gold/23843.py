
table = [1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536]

n, m = map(int, input().split())
value = list(map(int, input().split()))
result = 0

for i in value:
    if i != 1:
        result += table.index(i)
    else:
        result += 1
print(result)

# 틀림




