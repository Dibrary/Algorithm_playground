

from itertools import combinations

def isPrime(n):
    for i in range(2, n//2):
        if n%i == 0:
            return False
    return True

def solution(nums):
    tmp = set(nums)
    result = 0
    for i in combinations(tmp, 3):
        if isPrime(sum(i)):
            result += 1

    return result




## 다른 사람 코드 ##

from itertools import combinations
def prime_number(x):
    answer = 0
    for i in range(1,int(x**0.5)+1):
        if x%i==0:
            answer+=1
    return 1 if answer==1 else 0

def solution(nums):
    return sum([prime_number(sum(c)) for c in combinations(nums,3)])








def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(nums):
    from itertools import combinations
    comb = list(combinations(nums, 3))
    cnt = 0
    for tup in comb:
        if is_prime(sum(tup)):
            cnt += 1
    return cnt