
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        k = list(text)
        cnt = 0
        while True:
            for i in "balloon":
                if i in k:
                    k.remove(i)
                else:
                    return cnt
            cnt += 1





## 다른 사람 코드 ##

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count_b = text.count('b')
        if(count_b == 0):
            return 0
        count_a = text.count('a')
        if(count_a == 0):
            return 0
        count_l = text.count('l')
        if(count_l == 0):
            return 0
        count_o = text.count('o')
        if(count_o == 0):
            return 0
        count_n = text.count('n')
        if(count_n == 0):
            return 0
        min_count = min(count_b,count_a,count_l//2,count_o//2,count_n)
        return min_count





import collections

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        c = collections.Counter(text)
        return min(c['b'], c['a'], c['l'] // 2, c['o'] // 2, c['n'])
