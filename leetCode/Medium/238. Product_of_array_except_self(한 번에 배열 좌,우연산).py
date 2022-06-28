
class Solution:
    def productExceptSelf(self, nums):
        result = []

        start = 1
        for k in range(0, len(nums)):
            result.append(start)
            start = start*nums[k]

        # print(result) # 해당 start 위치 왼쪽 까지의 곱셈값이 리스트에 들어간다.

        start = 1
        for i in range(len(nums) -1, -1, -1): # 왼쪽으로 가면서 곱셈이 이뤄진다.

            result[i] = result[i]*start
            start = start*nums[i]

        return result


