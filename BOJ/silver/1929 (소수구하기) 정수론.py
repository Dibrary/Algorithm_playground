# sympy는 백준에서 못 쓴다.

# 기존 방식으로는 속도에 걸린다. (최대 1000000이 주어짐)

# import math
#
# tmp = [x for x in range(1000001)]
#
# for k in range(2, int(math.sqrt(1000001))):
#     for i in range(2, 100):
#         tmp[k*i] = 0
#
# n, m = map(int, input().split())
# result = [x for x in tmp[m:n+1] if x != 0]
# for k in result:
#     print(k)

# 위 코드는 1%부터 틀렸다고 나옴.



# import math
#
# def primenumber(x):
#     for i in range (2, int(math.sqrt(x) + 1)):	# 2부터 x의 제곱근까지의 숫자
#     	if x%i == 0:		# 나눠떨어지는 숫자가 있으면 소수가 아님
#         	return False
#     return True				# 전부 나눠떨어지지 않는다면 소수임
#
# m, n = map(int, input().split())
# for k in range(m, n+1):
#     if primenumber(k):
#         print(k)
        
# 위 코드는 pypy로 마지막에 틀림.

# import math
#
# s = 1000000  # 2부터 1000000까지 모든 수에 대하여 소수를 찾을 것이다.
# array = [True for i in range(s + 1)]  # 0,1을 제외한 모든 숫자가 소수(True)인 것으로 설정하고 시작한다.
#
#          # 에라토스테네스의 체 알고리즘
# for i in range(2, int(math.sqrt(s)) + 1):  # 2부터 n의 제곱근까지의 모든 수를 확인
#     if array[i] == True:  # i가 소수인 경우
# # i를 제외한 i의 모든 배수를 지우기
#         j = 2
#         while i * j <= s:
#             array[i * j] = False
#             j += 1
#
# m, n = map(int, input().split())
# for k in range(m, n+1):
#     if array[k]:
#         print(k)

# 89%에서 틀림


m, n = map(int, input().split())

for i in range(m, n+1):
    if i == 1:#1은 소수가 아니므로 제외
        continue
    for j in range(2, int(i**0.5) + 1):
        if i%j == 0: #약수가 존재하므로 소수가 아님
            break   #더이상 검사할 필요가 없으므로 멈춤
    else:
        print(i)
# 위 코드는 통과함. 왜?


## 다른 사람 코드 ##
def isPrime(num):
    if num==1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                return False
        return True

M, N = map(int, input().split())

for i in range(M, N+1):
    if isPrime(i):
        print(i)








m, n = map(int, input().split())
r =  set(range(m, n+1))
r -= {1}
y = int(n**0.5) +1
for i in range(2, y):
    r -= set(range(i*2, n+1, i))

r = sorted(list(r))
for i in r:
    print(i)











m, n = map(int, input().split())
is_prime = [True] * (n + 1)
is_prime[1] = False
for i in range(2, int(n ** 0.5) + 1):
    if not is_prime[i]:
        continue
    j = i
    while i * j <= n:
        is_prime[i * j] = False
        j += 1
for i in range(m, n + 1):
    if is_prime[i]:
        print(i)