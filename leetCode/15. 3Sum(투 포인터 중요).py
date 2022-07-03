
'''
for문을 3번 겹치면 (전수조사)
3000^3이 되어버림. 너무 오래 걸리지 않나?
'''
#
# class Solution:
#     def threeSum(self, nums):
#         result = []
#
#         for k in range(0, len(nums)):
#             for j in range(k+1, len(nums)):
#                 if nums[k]+nums[j] > 0 and nums.count(-(nums[k]+nums[j])) != 0:
#                     result.append([nums[k], nums[j], -(nums[k]+nums[j])])
#                 elif nums[k]+nums[j] < 0 and nums.count((nums[k]+nums[j])) != 0:
#                     result.append([nums[k], nums[j], (nums[k] + nums[j])])
#         print(result)


# 위 코드로 하면 O(n^2)까지 줄일 수 있음.
# 중복 제거가 안 된다.



class Solution:
    def threeSum(self, nums):
        result = []

        for k in range(0, len(nums)-1):
            for j in range(k+1, len(nums)):
                if nums[k]+nums[j] > 0 and nums.count(-(nums[k]+nums[j])) != 0:
                    tmp = [nums[k], nums[j], -(nums[k]+nums[j])]
                    tmp.sort()
                    if tmp not in result:
                        result.append(tmp)
                elif nums[k]+nums[j] < 0 and nums.count((nums[k]+nums[j])*(-1)) != 0:
                    tmp = [nums[k], nums[j], (nums[k] + nums[j])]
                    tmp.sort()
                    if tmp not in result:
                        result.append(tmp)
        return result

## 위 방식으로 해도 결과 안맞음, count는 단순히 중복된 것이 있어도 있다고 치기 때문;;



k = Solution()
print(k.threeSum([-1,0,1,2,-1,-4]))
print(k.threeSum([]))
print(k.threeSum([0]))







### 책 풀이 ###

### 브루트 포스 책 풀이 ###

class Solution:
    def threeSum(self, nums):
        results = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 1):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                for k in range(j + 1, len(nums)):
                    if k > j + 1 and nums[k] == nums[k - 1]:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        results.append([nums[i], nums[j], nums[k]])
        return results


'''
브루트 포스 방식은 O(n^3)의 시간이 걸려서 시간초과 나온다.
'''


### 투포인터 책 풀이 ###

class Solution:
    def threeSum(self, nums):
        results = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    results.append([nums[i], nums[left], nums[right])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return results


'''
투 포인터를 사용해서 O(n^2)로 시간복잡도를 줄였다.
'''

