
'''
왜 이게 DFS문제인지 모르겠고, (책은 단순히 가지치기를 해서 들어가기 때문이라는데.;;)
단순한 소수 판별 함수

'''


# 책 풀이 #
import sys
input = sys.stdin.readline

def isPrime(num): # 소수 판별 함수
    for i in range(2, num//2):
        if num%i == 0:
            return False # 여기를 만족하지 않으면 출력 이뤄지지 않은채로 백트래킹이 이뤄진다.
    return True

def dfs(number, j):
    if j == n:
        if isPrime(number): # 소수에 해당되면 
            print(number) # 출력한다
        return
    for i in range(1, 10):
        if i%2 == 0: # 짝수라면 탐색할 필요 없다.
            continue
        if isPrime(number*10 + i): # 소수라면
            dfs(number*10+i, j+1) # 재귀 함수로 자릿수를 늘린다.


n = int(input())
dfs(2, 1)
dfs(3, 1)
dfs(5, 1)
dfs(7, 1)



## 다른 사람 코드 ##

def isPrime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    if n < 9:
        return True
    k, l = 5, n**0.5
    while k <= l:
        if n % k == 0 or n % (k+2) == 0:
            return False
        k += 6
    return True

N = int(input())

def dfs(s):
    if len(s) > N:
        return
    n = int(s)
    if isPrime(n):
        if len(s) == N:
            print(n)
            return
        for i in [1, 3, 7, 9]:
            dfs(f'{n}{i}')

for i in [2, 3, 5, 7]:
    dfs(f'{i}')







n=int(input())

# 소수 판별
def isPrime(a):
    if(a<2):
        return False
    for i in range(2,int(a**0.5)+1):
        if(a%i==0):
            return False
    return True

def dfs(num):
	# 목표 길이 도달 시 멈춤
    if len(str(num))==n:
        print(num)
    else:
        for i in range(10):
            temp=num*10+i
            if isPrime(temp):
                dfs(temp)

dfs(2)
dfs(3)
dfs(5)
dfs(7)