'''
연결 리스트가 주어지고,
n차 회전을 했을 때의 값으로 연결 리스트를 수정하자.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def component_rotate(self, nums, k):
        result = [0] * len(nums)
        idx = k

        for i in nums:
            if idx > len(nums) - 1:
                idx -= len(nums)
            result[idx] = i
            idx += 1
        return result

    def rotatRight(self, head, k):
        nums = []
        while head != None:
            nums.append(head.val)
            head = head.next



if __name__=="__main__":
    k = Solution()
    v = k.rotatRight()

    while v != None:
        print(v.val)
        v = v.next