
'''
입력이 2진수인데 문자열로 주어짐..
'''

def func(s):
    tmp = 0
    for x in range(len(s)):
        tmp += int(s[x]) * (2 ** x)
    return tmp

def solution(bin1, bin2):
    bin1 = func(bin1[::-1])
    bin2 = func(bin2[::-1])

    result = bin(bin1+bin2)[2:]
    return result





## 다른 사람 코드 ##

def solution(bin1, bin2):
    answer = bin(int(bin1,2) + int(bin2,2))[2:]
    return answer









def solution(bin1, bin2):

    bin1 = '0b' + str(bin1)
    bin2 = '0b' + str(bin2)

    return bin(int(bin1,2) + int(bin2,2))[2:]