'''

'''


class Solution:
    def singleNumber(self, nums):
        tmp = dict();
        stand = set(nums)

        for i in nums:
            if i not in tmp:
                tmp[i] = 1
            else:
                tmp[i] += 1

        for i in stand:
            if tmp[i] == 1:
                return i
            else:
                pass

if __name__=="__main__":
    print(Solution().singleNumber([4,1,2,1,2]))