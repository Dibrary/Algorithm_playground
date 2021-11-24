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




