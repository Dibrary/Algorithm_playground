class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        cnt = 0

        for i in stones:
            for k in jewels:
                if k == i:
                    cnt += 1
        return cnt


### 다른 사람 코드 ###
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        jewel_count = 0

        for stone in stones:
            if stone in jewels:
                jewel_count += 1

        return jewel_count


### 책 풀이 ###
class Solution:
    def numJewelsInStones(self, J, S):
        freqs = {}
        count = 0

        for char in S:
            if char not in freqs:
                freqs[char] = 1
            else:
                freqs[char] += 1

        for char in J:
            if char in freqs:
                count += freqs[char]

        return count


from collections import defaultdict

class Solution:
    def numJewelsInStones(self, J, S):
        freqs = defaultdict(int)
        count = 0

        for char in S:
            freqs[char] += 1

        for char in J:
            count += freqs[char]

        return count


from collections import Counter


class Solution:
    def numJewelsInStones(self, J, S):
        freqs = Counter(S)
        count = 0

        for char in J:
            count += freqs[char]
        return count



class Solution:
    def numJewelsInStones(self, J, S):
        return sum(s in J for s in S)