
# arr = []
#
# for _ in range(9):
#     arr.append(int(input()))
#
# total = sum(arr)
# print(total, "total")
#
# for i in range(len(arr)-1):
#     for j in range(i+1, len(arr)):
#         if (total - arr[i]) - arr[j] == 100:
#             arr.remove(arr[i])
#             arr.remove(arr[j]) # 이렇게 해 버리면, 앞에서 변경된 arr의 j 인덱스 값이 적용되어서 원하는 결과가 안 됨.
#             break
# arr.sort()
# for k in arr:
#     print(k)

# 7%에서 틀림

arr = []

for _ in range(9):
    arr.append(int(input()))

total = sum(arr)

for i in range(len(arr)-1): # 이 부분이 다르긴 하다..
    for j in range(i+1, len(arr)):
        if total - (arr[i] + arr[j]) == 100:
            first = arr[i]
            second = arr[j]

            arr.remove(first)
            arr.remove(second)
            break
arr.sort()
for k in arr:
    print(k)

# 14%에서 틀림


## 다른 사람 코드 ##

import sys

tall_list = [int(sys.stdin.readline().strip()) for i in range(9)]

for i in range(len(tall_list)) :
    for j in range(i+1,len(tall_list)) :
        if tall_list[i] + tall_list[j] == sum(tall_list) - 100 :# 직접 입력
            a = tall_list[i]
            b = tall_list[j]
            tall_list.remove(a)
            tall_list.remove(b)
            break

tall_list.sort()

for i in tall_list :
    print(i)

## 왜 통과가 안 되었는지 차이를 모르겠다.



