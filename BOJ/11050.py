'''
바로 이항계수 구하기.
'''

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n*factorial(n-1)

n, k = list(map(int, input().split()))

print(int(factorial(n)/(factorial(k)*factorial(n-k))))