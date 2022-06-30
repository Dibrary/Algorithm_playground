'''
두 개의 숫자가 target값을 구성할 경우,
해당 숫자의 index를 반환.
(반환 시 시작 index는 1부터 시작하게)
'''


class Solution:
    def twoSum(self, numbers, target):
        tmp = dict()

        for i in range(0, len(numbers)):
            if (target - numbers[i]) not in tmp:
                tmp[numbers[i]] = i + 1
            elif (target - numbers[i]) in tmp:
                return sorted([i + 1, tmp[target - numbers[i]]])



if __name__=="__main__":
    k = Solution()
    print(k.twoSum([2,7,11,15],9))
    print(k.twoSum([2,3,4], 6))
    print(k.twoSum([-1,0],-1))




### 다른 사람 코드 ###
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = numbers
        l, r = 0, len(nums) - 1

        while l < r:
            curSum = nums[l] + nums[r]

            if curSum < target:
                l += 1
            elif curSum > target:
                r -= 1
            else:
                return [l + 1, r + 1]




class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s, e = 0, len(numbers)-1
        while s < e:
            if numbers[s] + numbers[e] == target:
                return [s+1, e+1]
            if numbers[s] + numbers[e] > target:
                e-=1
            else:
                s +=1
        return []



### 책 풀이 ###


from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while not left == right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return left + 1, right + 1  # 리턴 값 +1




from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for k, v in enumerate(numbers):
            left, right = k + 1, len(numbers) - 1
            expected = target - v
            # 이진 검색으로 나머지 값 판별
            while left <= right:
                mid = left + (right - left) // 2
                if numbers[mid] < expected:
                    left = mid + 1
                elif numbers[mid] > expected:
                    right = mid - 1
                else:
                    return k + 1, mid + 1



import bisect
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for k, v in enumerate(numbers):
            expected = target - v
            i = bisect.bisect_left(numbers[k + 1:], expected)
            if i < len(numbers[k + 1:]) and numbers[i + k + 1] == expected:
                return k + 1, i + k + 2




import bisect
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for k, v in enumerate(numbers):
            expected = target - v
            nums = numbers[k + 1:]
            i = bisect.bisect_left(nums, expected)
            if i < len(nums) and numbers[i + k + 1] == expected:
                return k + 1, i + k + 2






import bisect
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for k, v in enumerate(numbers):
            expected = target - v
            i = bisect.bisect_left(numbers, expected, k + 1)
            if i < len(numbers) and numbers[i] == expected:
                return k + 1, i + 1
