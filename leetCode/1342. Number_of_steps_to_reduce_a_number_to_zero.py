'''
2로 나누거나 1을 빼는 연산만 해서, 주어진 값이 0이 되게 만드는 '횟수'를 반환하자.
'''

class Solution:
    def numberOfSteps(self, nums: int) -> int:
        cnt = 0
        while nums != 0:
            if nums%2 == 0:
                nums = int(nums/2)
                cnt += 1
            else:
                nums -= 1
                cnt += 1
        return cnt

if __name__=="__main__":
    k = Solution()
    k.numberOfSteps(14)