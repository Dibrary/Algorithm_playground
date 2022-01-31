class Solution:
    def minSubsequence(self, nums):
        nums.sort(reverse=True)

        for k in range(0, len(nums)):
            if sum(nums[:k]) >= sum(nums[k + 1:]):
                return nums[:k]

# 위 코드 틀림

