
class Solution:
    def swapPairs(self, head):
        cur = head

        while cur and cur.next:
            cur.val, cur.next.val = cur.next.val, cur.val # 값 교환
            cur = cur.next.next # 다다음 노드로 곧바로 이동

        return head


