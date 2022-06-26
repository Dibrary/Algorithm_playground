'''
주어진 n값을 숫자를 더해서 만들 수 있는 모든 경우의수 구하기.

제한 : 1 <= n <= 45
'''

class Solution:
    def __init__(self):
        self.tmp = [False]*60

    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        elif n < 0:
            return 0

        if self.tmp[n] == False:
            self.tmp[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        else:
            return self.tmp[n]
        return self.climbStairs(n-1) + self.climbStairs(n-2)



if __name__=="__main__":
    k = Solution()
    print(k.climbStairs(40)) # 메모이제이션 안 쓰면 40만 가도 시간이 너무 오래 걸려서 통과가 안 됨.

