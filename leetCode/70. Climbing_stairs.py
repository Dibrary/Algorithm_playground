'''
주어진 n값을 숫자를 더해서 만들 수 있는 모든 경우의수 구하기.

제한 : 1 <= n <= 45
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        if n < 0:
            return 0
        return self.climbStairs(n-1) + self.climbStairs(n-2)

if __name__=="__main__":
    k = Solution()
    print(k.climbStairs(40)) # 40만 가도 시간이 너무 오래 걸려서 통과가 안 됨.

