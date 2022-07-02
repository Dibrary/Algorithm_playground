
# class Solution:
#     def containsNearbyDuplicate(self, nums, k):
#         check = set()
#         for idx, k in enumerate(nums):
#             if k in check: # 이미 확인한 숫자
#                 continue
#             elif k not in check: # 그렇지 않은 숫자
#                 check.add(k) # 우선 확인한걸로 담고
#
#                 for index, value in enumerate(nums):
#                     pass

                ## 근데 이렇게 하면 10만*10만이 되버려서 시간초과 될 듯.


class Solution:
    def containsNearbyDuplicate(self, nums, k):
        for idx, value in enumerate(nums):
            left = idx-k
            right = idx+k
            if left < 0 and right < len(nums):
                if nums[right] == value:
                    return True
            elif right >= len(nums) and left > 0:
                if nums[left] == value:
                    return True
            elif right < len(nums) and left > 0: # 2곳 모두 nums 범주 안에 있는 경우
                if nums[left] == value or nums[right] == value:
                    return True
        return False


tmp = Solution()
print(tmp.containsNearbyDuplicate([1,2,3,1],3))
print(tmp.containsNearbyDuplicate([1,0,1,1],1))
print(tmp.containsNearbyDuplicate([1,2,3,1,2,3],2))
print(tmp.containsNearbyDuplicate([1],1))

print(tmp.containsNearbyDuplicate([99,99],2)) # 이게 True가 나와야 한다고 함.






### 다른 사람 코드 ###





