
class Solution:
    def summaryRanges(self, nums):
        if nums == []:
            return []
        start = nums[0]
        temp = nums[0]

        result = []
        for index in range(1, len(nums)):

            if nums[index] - temp == 1:
                temp = nums[index]
            else: # 차이가 1보다 크면
                if start != temp:
                    result.append(f"{start}->{temp}")
                else:
                    result.append(f"{temp}")
                start = nums[index]
                temp = nums[index]

        if start != temp: # 맨 끝에 값을 처리하기 위해 if-else문이 한 번 더 쓰인 것.
            result.append(f"{start}->{temp}")
        else:
            result.append(f"{temp}")

        return result


tmp = Solution()
print(tmp.summaryRanges([0,1,2,4,5,7]))
print(tmp.summaryRanges([0,2,3,4,6,8,9]))



### 다른 사람 코드 ###
from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        out = []
        nums.append(' ')
        beg, prev = nums[0], nums[0]
        for i in nums[1:]:
            if i == prev + 1:
                prev = i
                continue
            elif prev == beg:
                out.append(str(beg))
            else:
                elem = str(beg) + "->" + str(prev)
                out.append(elem)
            beg, prev = i, i
        return out




class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if nums:
            nums += [float("inf")]
        res = []
        j = 0
        for i in range(len(nums)):
            if i != j and nums[i] - nums[i - 1] > 1:
                if i - 1 - j == 0:
                    res.append(str(nums[i - 1]))
                else:
                    res.append(str(nums[j]) + "->" + str(nums[i - 1]))
                j = i
        return res






class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges, r = [],[]
        for n in nums:
            if n-1 not in r:
                r = []
                ranges += r,
            r[1:] = n,
        return['->'.join(map(str,r)) for r in ranges]






class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []

        s = ""

        for i in range(len(nums)):
            if len(s) == 0:
                s = str(nums[i])

            if i == len(nums) - 1 or nums[i + 1] != nums[i] + 1:
                if s == str(nums[i]):
                    result.append(s)
                else:
                    s += "->" + str(nums[i])
                    result.append(s)
                s = ""
        return result