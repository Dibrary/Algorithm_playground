
from itertools import permutations

class Solution:
    def permute(self, nums):
        result = []
        for i in permutations(nums, len(nums)):
            result.append(i)
        return result


### 다른 사람 코드 ###
class Solution:
    def permute(self, nums):
        result = []
        if len(nums) == 1:
            return [nums[:]]

        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)

            result.extend(perms)
            nums.append(n)

        return result


class Solution:
    def permute(self, nums):

        def dfs(nums, path, res):
            if len(nums) == 0:
                res.append(path)
            for i in range(0, len(nums)):
                dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)

        res = []
        dfs(nums, [], res)
        return res


    ### 책 풀이 ###
'''
레벨이 증가할 수록 한 노드로부터 자식노드의 수는 점점 작아진다.
'''

class Solution:
    def permute(self, nums):
        results = []
        prev_elements = []

        def dfs(elements):
            if len(elements) == 0: # leaf node일 때 결과를 추가한다.
                results.append(prev_elements[:])

            for e in elements: # 순열 생성을 하는 재귀 호출.
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()
        dfs(nums)
        return results



class Solution:
    def permute(self, nums):
        return list(permutations(nums))