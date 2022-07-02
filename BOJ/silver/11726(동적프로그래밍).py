
# n = int(input())
#
# arr = [0,1,2]
# if n <= 2:
#     print(arr[n])
# else:
#     for k in range(2, n+1):
#         arr.append(arr[k]+arr[k-1])
# print(arr[n])

# 곧바로 틀려버림
# 아 값을 10007로 나눈 나머지를 출력해야 한다.


# n = int(input())
#
# arr = [0,1,2]
# if n <= 2:
#     print(arr[n]%10007)
# else:
#     for k in range(2, n+1):
#         arr.append(arr[k]+arr[k-1])
# print(arr[n]%10007)


## 끝에 ? 가서 틀렸다.

n = int(input())

arr = [0,1,2]

for k in range(2, 1001):
    arr.append(arr[k] + arr[k - 1])

print(arr[n]%10007)

# 20  [0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711]




### 다른 사람 코드 ###

s = [0, 1, 2]
for i in range(3, 1001):
  s.append(s[i - 2] + s[i - 1])
n = int(input())
print(s[n] % 10007)




n = int(input())

c = [0 for i in range(1001)]
c[1] = 1
c[2] = 2

for i in range(3, n+1):
    c[i] = c[i-1] + c[i-2]
print((c[n]%10007))
