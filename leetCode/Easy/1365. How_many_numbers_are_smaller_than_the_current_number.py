'''
해당  index의 값과 나머지 위치의 값들과 비교해서, 작은 것의 갯수를
차례대로 리스트에 담아서 반환한다.
'''

class Solution:
    def smallerNumbersThanCurrent(self, nums):
        result = []

        for i in range(0, len(nums)):
            tmp = nums[:i] + nums[i + 1:]
            cnt = 0
            for j in range(0, len(tmp)):
                if nums[i] > tmp[j]:
                    cnt += 1
                else:
                    pass
            result.append(cnt)
        return result


if __name__ == "__main__":
    k = Solution()
    print(k.smallerNumbersThanCurrent([8, 1, 2, 2, 3]))