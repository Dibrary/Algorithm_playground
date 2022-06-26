'''
사이클이 생성되는 연결 리스트인지를 판단하자.
'''

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head):
        tmp = set()
        while head.next != None:
            if (head.val, head.next.val) not in tmp:
                tmp.add((head.val, head.next.val))
            else:
                return True
        return False # [] 라는 케이스에서 통과 못함.. []가 뭔지 모르겠음,
    # 혹시 몰라서 None으로만 구성된 cycle 리스트를 만들어도 True나옴.


if __name__=="__main__":
    k = Solution()
    d = ListNode(4)
    c = ListNode(3)
    b = ListNode(2)
    a = ListNode(1)
    a.next = b
    b.next = c
    c.next = d
    d.next = b

    print(k.hasCycle(a))

# 다른 시도

class Solution:
    def hasCycle(self, head):
        cnt = 0

        single = []
        double = []

        while head:
            if cnt % 2 == 0:
                double.append(head.val)
                single.append(head.val)
                head = head.next
            else:
                single.append(head.val)
                head = head.next
            cnt += 1

            if single[-1] == double[-1]:
                return True

        return False

# [1] 에서 True가 나와야 하는데 False가 나온다고 Wrong됨.

