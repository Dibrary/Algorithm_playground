#
# n = int(input())
#
# arr = [x for x in range(n+1)]
#
# result = []
# for k in range(1, n//2):
#     while k < len(arr):
#         result.append(arr[k])
#         k = k+2
# print(result)

# 위 코드는 예제 결과가 좀 다르게 나온다.

n = int(input())

arr = [x for x in range(1, n+1)]

result = []
while len(arr) != 1:
    result.append(arr.pop(0))
    tmp = arr.pop(0)
    arr.append(tmp)
result.append(arr.pop(0))
print(" ".join(map(str,result)))