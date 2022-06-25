
class Solution:
    def majorityElement(self, nums):
        standard = len(nums)/3

        result = []
        tmp = set(nums)
        for k in tmp:
            if nums.count(k) > standard:
                result.append(k)
        result.sort()
        return result

# ?? medium인데 한 번에 됨


