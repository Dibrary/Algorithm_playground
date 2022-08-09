
max_v = 1200000

sieve = [True] * (max_v+100)
sieve[0] = False; sieve[1] = False
sieve[2] = True

prime = 2
while prime * prime <= max_v:
    if not sieve[prime]:
        prime += 1
        continue
    for t in range(2 * prime, max_v + 3, prime):
        sieve[t] = False
    prime += 1
# 이 sieve 방법을 반드시 기억해두자. 이게 속도가 빠르게 진행된다.

n = int(input())
for k in range(n, max_v):
    if sieve[k] != 0:
        string = str(k)
        if string == string[::-1]:
            print(string)
            break


## 다른 사람 코드 ##

from sys import stdin
input = stdin.readline

def isPalindrome(n):
    length = len(n) // 2
    for i in range(length):
        if n[i] != n[-i-1]:
            return False
    return True

def isPrimeNumber(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if not n%i:
            return False
    return True

# main
N = int(input())
while True:
    if isPalindrome(str(N)) and isPrimeNumber(N):
        break
    N += 1
print(N)









l=[0, 0, *range(2,10**6),(10**6)+3001] # list안에서 *붙이고 range를 사용하면 알아서 풀린다.

for i in l:
    if i:
        for j in range(i*i, 10**6, i):
            l[j] = 0
n = int(input())
print(min(i for i in filter(int, l)if i >= n and str(i) == str(i)[::-1]))