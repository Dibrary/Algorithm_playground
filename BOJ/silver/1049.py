#
# import sys
#
# n, m = list(map(int, sys.stdin.readline().split()))
# strings = []
#
# for _ in range(m):
#     six, one = list(map(int, sys.stdin.readline().split()))
#     strings.append((six, one))
# strings.sort(key=lambda x:x[0])
#
# value1 = n/6
# value2 = n%6
# value3 = value1+1
#
# tmp3 = (value3*strings[0][0])
# tmp1 = (value1*strings[0][0])
#
# strings.sort(key=lambda x:x[1])
# tmp2 = (value2*strings[0][1])
#
# print(tmp3, tmp1, tmp2)
# if tmp3 < tmp1+tmp2:
#     print(tmp3)
# else:
#     print(tmp1+tmp2)

'''
6 1
7 1 이게 반례다. (정답은 6이 나와야 됨)
위 반례는 낱개로 한 6개의 가격이 6개들이 가격보다 작다. 즉, 이걸 거르는 코드가 추가로 있어야 함.
'''
#
# n, m = map(int, input().split())
#
# strings = []
# for _ in range(m):
#     strings.append(list(map(int, input().split())))
#
# result = 0
# if n < 6:
#     tmp = [x[1]*n for x in strings]
#     print(min(tmp))
#
# else: # 6보다 크다면,
#     results = [] # 답만 모아두는 변수
#     for k in strings:
#         if k[0]*6 < k[1]*6:
#             results.append(k[1]*n)
#         else:
#             results.append((k[0]*(n//6))+(k[1]*(n%6)))
#     print(min(results))

# 위 코드로 하면 안 된다. 6개들이랑 1개짜리를 꼭 같은 곳에서 살 필요는 없다.


# n, m = map(int, input().split())
#
# six_strings = []
# one_strings = []
# for _ in range(m):
#     six, one = map(int, input().split())
#     six_strings.append(six)
#     one_strings.append(one)
#
# result = 0
# if n < 6:
#     tmp = [x*n for x in one_strings]
#     print(min(tmp))
#
# else: # 6보다 크다면,
#     results = [] # 답만 모아두는 변수
#     one_min = min([m*6 for m in one_strings])
#
#     if min([k*(n//6) for k in six_strings]) > one_min: # 6개들이 중 가장 싼 가격이 1개짜리로 사는 가장 싼 거보다 비싸면,
#         if min([k*(n//6+1) for k in six_strings]) < (min([k*(n//6) for k in six_strings])+min([m*(n%6) for m in one_strings])):
#             print(min([k*(n//6+1) for k in six_strings]))
#         else:
#             print(min([m*n for m in one_strings]))
#     else:
#         if min([k*(n//6+1) for k in six_strings]) < (min([k*(n//6) for k in six_strings])+min([m*(n%6) for m in one_strings])):
#             print(min([k*(n//6+1) for k in six_strings]))
#         else:
#             print(min([k*(n//6) for k in six_strings])+min([m*(n%6) for m in one_strings]))

# 9%에서 틀림.

n, m = map(int, input().split())

min_p = 10001
min_s = 10001

for _ in range(m):
    p, s = map(int, input().split())
    min_p = min(p, min_p)
    min_s = min(s, min_s)

if min_p > min_s*6:
    print(min_s*n)
else:
    result = (n//6)*min_p
    if (n%6)*min_s > min_p: # 여기가 핵심 코드다.
        result += min_p
    else:
        result += (n%6)*min_s
    print(result)









## 다른사람 코드

n, m = map(int, input().split())

answer = 0
price_list = []

for _ in range(m):
    price = tuple(map(int, input().split()))
    price_list.append(price)

six_list = sorted(price_list, key=lambda x : x[0])
one_list = sorted(price_list, key=lambda x : x[1])

if six_list[0][0] <= one_list[0][1] * 6:
    answer = six_list[0][0] * (n // 6) + one_list[0][1] * (n % 6)
    if six_list[0][0] < one_list[0][1] * (n % 6):
        answer = six_list[0][0] * (n//6 + 1)
else:
    answer = one_list[0][1] * n

print(answer)




## 다른사람 코드
import sys

input = sys.stdin.readline

N, M = map(int, input().split(' '))

minPack = 1001 # 주어지는 입력보다 더 큰 값으로 초기화
minSingle = 1001
for i in range(M):
  p, s = map(int, input().split(' '))
  minPack = min(minPack, p)
  minSingle = min(minSingle, s)

result = 0

# 패키지가 낱개 X 6 보다 가격이 크면 낱개로 모두가 구매한다.
if minPack > minSingle*6:
  result += N * minSingle
else:
  # 패키지가 더 저렴할 때
  # N을 6으로 나눈 몫 만큼 패키지로 구매 한다
  result += (N//6) * minPack

  # 남은 낱개의 가격이 패키지 보다 크면 패키지를 구매하고 아니면
  # 낱개로 구매한다.
  if (N%6)*minSingle > minPack:
    result += minPack
  else:
    result+= (N%6)*minSingle

print(result)

