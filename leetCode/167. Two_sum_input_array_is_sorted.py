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