'''
자리수를 자른 후에 제곱해서 다시 더하고 while로 무한루프 하면 될 줄 알았는데,
주어지는 숫자 범위가... 1 <= n <= 2**31 - 1

자릿수가 너무 크다.

'''


class Solution:
    def isHappy(self, n):
        if len(str(n)) == 1:
            n = n**2



