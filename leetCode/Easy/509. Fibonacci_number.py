
class Solution:
    def fib(self, n: int) -> int:
        if n == 1 : return 1
        if n == 0 : return 0
        return self.fib(n-1)+self.fib(n-2)



### 다른 사람 코드 ###

class Solution:
    def fib(self, n: int) -> int:

        if n <= 1: return n
        prev, curr = 0, 1
        for i in range(2, n + 1):
            curr, prev = prev + curr, curr
        return curr




class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        for i in range(1, n + 1):
            a, b = b, a + b
        return a

### 책 풀이 ###

class Solution:
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        return self.fib(N - 1) + self.fib(N - 2)






import collections


class Solution:
    dp = collections.defaultdict(int)

    def fib(self, N: int) -> int:
        if N <= 1:
            return N

        if self.dp[N]:
            return self.dp[N]
        self.dp[N] = self.fib(N - 1) + self.fib(N - 2)
        return self.dp[N]






import collections


class Solution:
    dp = collections.defaultdict(int)

    def fib(self, N: int) -> int:
        self.dp[0] = 0
        self.dp[1] = 1

        for i in range(2, N + 1):
            self.dp[i] = self.dp[i - 1] + self.dp[i - 2]
        return self.dp[N]






class Solution:
    def fib(self, N: int) -> int:
        x, y = 0, 1
        for i in range(0, N):
            x, y = y, x + y
        return x
