# nums1 = [1, 3, 5, 2, 4]
# nums2 = [6, 5, 4, 3, 2, 1, 7]
#
# result = []
# for i in nums1:
#     idx = nums2.index(i)
#
#     if idx == len(nums2) - 1:
#         result.append(-1)
#     elif nums2[idx + 1] > nums2[idx]:
#         result.append(nums2[idx + 1])
#     else:
#         if max(nums2[idx:]) > nums2[idx]:
#             result.append(max(nums2[idx:]))
#         else:
#             flag = 0
#             for j in nums2[idx:]:
#                 if j > i:
#                     result.append(j)
#                     flag = 1
#                     break
#             if flag == 0:
#                 result.append(-1)
# print(result)# 실패

'''
처음에 예제가 무슨 규칙을 가지는지 모르겠음

1번째 예는 4보다 큰 값은 없으므로 -1, 1보다 큰 값은 3이고,
2보다 큰 값은 없다. 


2번째 예는
2보다 큰 값이 3이고, 4보다 큰 값은 없으므로 -1

이 예제로 파악하면
1. 주어진 배열의 위치를 바꾸지 않는다.
2. 곧바로 다음 값에 대해서만 판단을 한다.

'''

class Solution:
    def nextGeneratorElement(self, nums1, nums2):
        result = []

        for target in nums1:
            target_index = nums2.index(target)
            tmp = nums2[target_index+1:]

            if tmp == []:
                result.append(-1)
            else:
                flag = 0
                for x in tmp:
                    if x > target:
                        result.append(x)
                        flag = 1
                        break
                if flag == 0:
                    result.append(-1)
        return result

k = Solution()
print(k.nextGeneratorElement([4,1,2],[1,3,4,2]))
print(k.nextGeneratorElement([2,4],[1,2,3,4]))

# 문제를 제대로 이해하는 게 중요하다.


### 다른 사람 코드 ###
from collections import defaultdict

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        d = defaultdict(int)
        stack = []
        for i, num in enumerate(nums2):
            while stack and nums2[stack[-1]] < num:
                d[nums2[stack.pop()]] = num
            stack.append(i)
        while stack:
            d[nums2[stack.pop()]] = -1

        res = []
        for x in nums1:
            res.append(d[x])
        return res



### 다른 사람 코드 ###
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        seen = {}
        stack = []
        result = [-1] * len(nums1)
        for idx, num in enumerate(nums1):
            seen[num] = seen.get(num, idx) # 전처리

        for idx, num in enumerate(nums2):
            while stack != [] and stack[-1] < num:
                value = stack.pop()
                idx = seen[value]
                result[idx] = num
            if num in seen:
                stack.append(num)

        return result