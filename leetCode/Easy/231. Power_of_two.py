'''
2의 제곱으로만 나타낼 수 있는지 판별하기
'''


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        elif n == 0:
            return False

        value = bin(n)[3:]

        if "1" in value:
            return False
        else:
            return True

if __name__=="__main__":
    print(Solution().isPowerOfTwo(16))
    print(Solution().isPowerOfTwo(8))
    print(Solution().isPowerOfTwo(0))
    print(Solution().isPowerOfTwo(1))