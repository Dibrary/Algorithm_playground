n = int(input())

arr = dict()
for _ in range(n):
    value = int(input())

    if value in arr:
        arr[value] += 1
    else:
        arr[value] = 1

max_cnt = max(arr.values())
min_value = 2 ** 62
for j in arr.items():
    if j[1] == max_cnt:
        if j[0] <= min_value:
            min_value = j[0]
print(min_value)

# 사전형에서 items와 values를 쓸 줄 알면 됨.