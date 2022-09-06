
# n = int(input())
#
# cnt = 0
# for s in range(1, n+1):
#     tmp = bin(s)[2:]
#     if tmp[0] == '1':
#         if '11' not in tmp:
#             cnt += 1
# print(cnt)

# 틀림

# 아 문제가 n까지의 2진수가 아니라 n자리 수의 가능한 경우의 수

n = int(input())

arr = [1, 1, 2]
for k in range(3, 91):
    arr.append(arr[k-1] + arr[k-2])

print(arr[n-1])


## 다른 사람 코드 ##

n = int(input())
count = 0

n_list = [0 for _ in range(91)]

n_list[1] = 1
n_list[2] = 1

for i in range(3,91):
    n_list[i] = n_list[i-1] + n_list[i-2]

print(n_list[n])









s = [0, 1, 1]
for i in range(3, 91):
    s.append(s[i - 2] + s[i - 1])
n = int(input())
print(s[n])