from itertools import combinations


class Solution:
    def combine(self, n: int, k: int):
        result = []

        for i in combinations([x for x in range(1, n + 1)], k):
            tmp = []
            for k in i:
                tmp.append(k)
            result.append(tmp)
        return result


### 다른 사람 풀이 ###
class Solution:
    def combine(self, n: int, k: int):

        return combinations(range(1,n+1),k)


from collections import deque

class Solution:
    def combine(self, n: int, k: int):
        result = deque([[]])

        for pos in range(k):
            positions_left = k - pos - 1

            n_comb = len(result)
            for _ in range(n_comb):
                sub_combination = result.popleft()
                start = (sub_combination[-1] + 1) if len(sub_combination) > 0 else 1
                for i in range(start, n + 1 - positions_left):
                    result.append(sub_combination + [i])

        return result

### 책 풀이 ###

class Solution:
    def combine(self, n, k):
        results = []

        def dfs(elements, start, k):
            if k == 0:
                results.append(elements[:])
                return

            for i in range(start, n+1):
                elements.append(i)
                dfs(elements, i+1, k-1)
                elements.pop()
        dfs([], 1, k)
        return results
