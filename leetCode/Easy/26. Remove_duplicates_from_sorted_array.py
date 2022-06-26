class Solution:
    def removeDuplicates(self, nums):
        tmp_idx = 1

        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                pass
            else:
                nums[tmp_idx] = nums[i]
                tmp_idx += 1
        return tmp_idx

if __name__=="__main__":
    k = Solution()
    print(k.removeDuplicates([0,1,2,2,2,2,3,3,4]))