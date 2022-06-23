
'''
배열을 입력받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력하기

전체 길이는 최대 100000까지 나올 수 있으니,
모든 경우의 수를 고려해도 100000*100000 인데.. 시간안에 될까?

각 값은 -30~30을 벗어나지 않는다.

You must write an algorithm that runs in O(n) time and without using the division operation.
이 문구대로면 O(n)만에 풀 수 있는 방법 찾아야됨.
'''


# class Solution:
#     def productExceptSelf(self, nums):
#         result = []
#         for i in range(len(nums)):
#             tmp = nums[:i]+nums[i+1:]
#             total = 1
#             for k in tmp: # for문을 2겹으로 돌기 때문에 O(n^2)이 됨.
#                 total *= k
#             result.append(total)
#         return result
#
#
# k = Solution()
# print(k.productExceptSelf([1,2,3,4]))

# 예상한대로 시간초과 걸림

'''
왼쪽 곱하는 것과
오른쪽 곱하는 것을 분리하면 for문이 별개로 돌 수 있나?
'''

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


k = Solution()
print(k.productExceptSelf([1, 2, 3, 4]))

