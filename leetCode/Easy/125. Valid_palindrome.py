'''
띄어쓰기와, 숫자를 제외한 나머지는 고려하지 않고,
palindrome을 만족하는지 판단해서 반환.
'''


class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1 and s.isalpha():
            return True
        result = ""
        for i in s:
            if i.isalpha() or i.isdigit():
                result += i.lower()

        start = 0
        end = len(result) - 1
        while start < end:
            if result[start] == result[end]:
                start += 1
                end -= 1
                pass
            else:
                return False
        return True

if __name__=="__main__":
    k = Solution()
    print(k.isPalindrome("OP"))



## 아래 출력부를 이렇게 수정하면 더 깔끔하다 ##

class Solution:
    def isPalindrome(self, s):
        if len(s) == 1 and s.isalpha():
            return True
        result = ""
        for i in s:
            if i.isalpha() or i.isdigit(): # 숫자 포함.
            # if i.isalnum(): 이렇게 하면 한 번에 숫자, 문자만 걸러낼 수 있다.
                result += i.lower()

        return True if result == result[::-1] else False
        # return result == result[::-1] 이렇게 해도 됨.


### 다른 사람 코드
import re

class Solution:
    def isPalindrom(self, s):
        s = s.lower()
        s = re.sub('[^a-z0-9]', '',s)
        return s == s[::-1]




