'''
여분의 list 할당 없이 수행해야 한다.
반환 값은 주어진 값을 제외한 나머지 해당 값의 갯수만.
주어진 list는 빠진 숫자를 제외하고 나머지가 앞에 위치해 있어야 한다. (정렬 무관)
'''
class Solution:

    def sorting(self, nums):
        start_idx = 0
        end_idx = len(nums) - 1

        while start_idx < end_idx:
            if nums[start_idx] == '' and nums[end_idx] != '':
                nums[start_idx], nums[end_idx] = nums[end_idx], nums[start_idx]
                start_idx += 1
                end_idx -= 1
            if nums[start_idx] != '':
                start_idx += 1
            if nums[end_idx] == '':
                end_idx -= 1

        return nums

    def removeElement(self, nums, val):
        cnt = 0
        for idx, v in enumerate(nums):
            if v == val:
                nums[idx] = ''
            else:
                cnt += 1
        return self.sorting(nums)

if __name__=="__main__":
    k = Solution()
    print(k.removeElement([3,2,2,3],3))
    print(k.removeElement([0,1,2,2,3,0,4,2],2))
