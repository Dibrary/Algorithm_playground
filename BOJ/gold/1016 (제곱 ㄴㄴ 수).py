
'''
min 최고 범주는 10**12 (1456번 문제의 최고 범주는 10**14였다.)
그러나, max 와 min 범주는 100만개 보다 작다.
따라서, for문이 돌더라도 100만개 까지밖에 순회를 안 한다.

'''


N = 10**6 + 10**5

sieve = [True]* (N+100) # 미리 다 구해놓는 코드.
sieve[0] = False

for k in range(2, N):
    pow = 2
    while k**pow <= len(sieve):
        sieve[k**pow] = False
        pow += 1
# 위 코드는 총 1.499초 걸린다.

min_value, max_value = map(int, input().split())

cnt = 0
for i in range(min_value, max_value+1):
    if sieve[i]:
        cnt += 1
print(cnt)

# Jupyter에서 돌리면 1 1000에 답이 960으로 나온다.;;
# 위 코드는 IndexError 발생한다.



## 다른 사람 코드 ##

min, max = map(int, input().split())

answer = max - min + 1
divisibleByTheSquare = [False] * (max-min+1)
# 첫 번째 값은 min값, 맨 끝 값은 max값의 boolean값이 되는 셈이다.

for i in range(2, int(max**0.5+1)):
    square = i**2

    for j in range((((min-1)//square) + 1)*square, max + 1, square):
        if not divisibleByTheSquare[j-min] : # j-min으로 함으로써 min값인 경우 0 index로 되게 함.
            divisibleByTheSquare[j-min] = True
            answer -= 1
print(answer)






import sys
input = sys.stdin.readline

def solution(MIN,MAX):
    answer = MAX-MIN+1
    check = [False]*(MAX-MIN+1)
    i = 2
    while i*i <= MAX:
        square_number = i*i #제곱수
        # remain
        # 제곱수가 딱 나누어 떨어지면 상관없지만 그게 아니라면 소수점이 버림 처리 된다.
        # 그래서 remain으로 그 값을 보정해준다.
        remain = 0 if MIN%square_number == 0 else 1

        j = MIN//square_number + remain #제곱수로 나눈 몫 => 배수

        while square_number*j <= MAX:   #제곱수의 j배 (에라토스테네스의 체)
            if not check[(square_number*j) - MIN]:
                check[(square_number*j) - MIN] = True
                answer -= 1
            j += 1#배수 점점 증가
        i += 1

    print(answer)
a,b = map(int,input().split())
solution(a,b)










from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    min_val, max_val = map(int, input().split())
    check = [True] * (max_val - min_val + 1)

    if max_val <= 3:
        print(max_val - min_val)
        exit()
    prime_square = [4]
    max_sqrt = int(max_val**0.5)
    is_prime = [True] * (max_sqrt // 2 + 1)
    for i in range(3, max_sqrt + 1, 2):
        if is_prime[i // 2]:
            i_square = i * i
            prime_square.append(i_square)
            is_prime[i_square // 2 :: i] = [False] * (
                (max_sqrt - i_square + 1) // (2 * i) + 1
            )
    for num in prime_square:
        st = num - min_val % num if min_val % num else 0
        check[st::num] = [False] * len(check[st::num])
    print(check.count(True))










from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    min_val, max_val = map(int, input().split())
    check = [False] * (max_val - min_val + 1)
    ans = max_val - min_val + 1
    for n in range(2, int(max_val**0.5) + 1):
        n_square = n * n
        q = min_val // n_square + 1 if min_val % n_square else min_val // n_square
        q_max = max_val // n_square + 1
        for k in range(q, q_max):
            if not check[n_square * k - min_val]:
                check[n_square * k - min_val] = True
                ans -= 1
    print(ans)

