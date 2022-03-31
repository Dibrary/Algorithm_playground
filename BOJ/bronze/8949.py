
a, b = input().split()
a = a[::-1] ; b = b[::-1] # 역순

min_length = min(len(a), len(b))

result = []
for i in range(min_length):
    result.insert(0,int(a[i]) + int(b[i]))

if len(a) > len(b):
    result.insert(0, int(a[min_length:]))
elif len(a) < len(b):
    result.insert(0, int(b[min_length:]))

print("".join(map(str, result)))

# 틀림 ;';


