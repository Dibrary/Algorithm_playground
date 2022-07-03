
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        result = 0
        try:
            result = nums.index(target)
            return result
        except:
            return -1


## 다른 사람 코드 ##

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            # left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # right sorted portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1







class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for idx, value in enumerate(nums):
            if value == target:
                return idx
        return -1



## 책 풀이 ##
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 예외 처리
        if not nums:
            return -1

        # 최소값 찾아 피벗 설정
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        pivot = left
        # 피벗 기준 이진 검색
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            mid_pivot = (mid + pivot) % len(nums)

            if nums[mid_pivot] < target:
                left = mid + 1
            elif nums[mid_pivot] > target:
                right = mid - 1
            else:
                return mid_pivot
        return -1







