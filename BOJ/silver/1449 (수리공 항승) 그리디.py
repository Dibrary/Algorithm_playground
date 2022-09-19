
n, l = map(int, input().split())
leaks = list(map(int, input().split()))

arr = set()

for k in leaks:
    arr.add(k-0.5)
    arr.add(k+0.5)
tmp = list(arr)
print(tmp)

'''
여기서 문제는 어떤 간격일 경우 띄고, 어떤 간격일 경우 그냥 붙여서 하나로 취급하느냐
'''

result = 0
for x in range(1, len(tmp)):
    if (tmp[x]-tmp[x-1]) <= length:
        length -= (tmp[x]-tmp[x-1])
        print(length, x, tmp[x], tmp[x-1])
    if length == 0:
        result += 1
        length = l

result += 1

# 이렇게 하면 딱 떨어지지 않는 경우는 답이 맞으나, 딱 떨어지는 경우는 답이 +1 된다.














