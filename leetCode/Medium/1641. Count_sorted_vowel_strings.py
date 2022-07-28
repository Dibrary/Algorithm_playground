'''
모음 갯수로 만들 수 있는 모든 경우의 수 찾기. (순서 무관)
'''

from itertools import combinations

class Solution:
    def countVowelStrings(self, n: int) -> int:
        cnt = 0
        for i in combinations([x for x in range(0, n+4)], n):
            cnt += 1
        return cnt

if __name__=="__main__":
    print(Solution().countVowelStrings(2))
    print(Solution().countVowelStrings(33))