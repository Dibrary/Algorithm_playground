'''
최솟값 만들기,
기준값보다 큰 값에 2진수 1의 갯수가 같은 값 중 가장 작은 값.
'''

def solution(n):
    for x in range(n+1, 1000080):
        if bin(n)[2:].count('1') == bin(x)[2:].count('1'):
            return x




## 다른 사람 풀이 ##

def nextBigNumber(n):
    num1 = bin(n).count('1')
    while True:
        n = n + 1
        if num1 == bin(n).count('1'):
            break
    return n





def nextBigNumber(n):
    c = bin(n).count('1')
    for m in range(n+1,1000001):
        if bin(m).count('1') == c:
            return m