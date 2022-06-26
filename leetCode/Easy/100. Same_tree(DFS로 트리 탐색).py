'''
2개의 트리가 같은지, 확인하기
'''

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class Solution:
#     def isSameTree(self, p, q):
#         first, second = [], []
#         queue = deque()
#
#         queue.append(p)
#         while len(queue) != 0:
#             node = queue.popleft()
#             first.append(node.val)
#             if node.left != None:
#                 queue.append(node.left)
#                 first.append(node.left.val)
#             elif node.left == None:
#                 first.append(0)
#
#             if node.right != None:
#                 queue.append(node.right)
#                 first.append(node.right.val)
#             elif node.right == None:
#                 first.append(0)
#
#         queue.append(q)
#         while len(queue) != 0:
#             node = queue.popleft()
#             second.append(node.val)
#             if node.left != None:
#                 queue.append(node.left)
#                 second.append(node.left.val)
#             elif node.left == None:
#                 second.append(0)
#
#             if node.right != None:
#                 queue.append(node.right)
#                 second.append(node.right.val)
#             elif node.right == None:
#                 second.append(0)
#         print(first, second)
#         return True if first == second else False


# class Solution:
#     def isSameTree(self, p, q):
        # queue1 = deque()
        # queue2 = deque()
        #
        # queue1.append(p)
        # queue2.append(q)
        # while len(queue1) != 0 and len(queue2) != 0:
        #     node1 = queue1.popleft()
        #     node2 = queue2.popleft()
        #
        #     if node1.val == node2.val:
        #         if node1.left != None and node2.left != None:
        #             queue1.append(node1.left)
        #             queue2.append(node2.left)
        #         elif node1.left == None and node2.left == None:
        #             queue1.append(TreeNode(None))
        #             queue2.append(TreeNode(None))
        #         if node1.right != None and node2.right != None:
        #             queue1.append(node1.right)
        #             queue2.append(node2.right)
        #         elif node1.right == None and node2.right == None:
        #             queue1.append(TreeNode(None))
        #             queue2.append(TreeNode(None))
        #         if node1.right == None and node1.left == None and node2.right == None and node2.right == None:
        #             return True
        #     else:
        #         return False
        #
        #     if node1.left == None and node2.left != None:
        #         return False
        #
        #     if node1.right == None and node2.right != None:
        #         return False
        # return True # [] 케이스는 통과하지 못함.. []가 뭔데?

from collections import deque

# class Solution:
#     def isSameTree(self, p, q):
#         vals_p = []
#         tmp_p = deque()
#         tmp_p.append(p)
#         while tmp_p:
#             now_node = tmp_p.popleft()
#             vals_p.append(now_node.val)
#             if now_node.left:
#                 tmp_p.append(now_node.left)
#             else:
#                 vals_p.append(None)
#             if now_node.right:
#                 tmp_p.append(now_node.right)
#             else:
#                 vals_p.append(None)
#
#         vals_q = []
#         tmp_q = deque()
#         tmp_q.append(q)
#         while tmp_q:
#             now_node = tmp_q.popleft()
#             vals_q.append(now_node.val)
#             if now_node.left:
#                 tmp_q.append(now_node.left)
#             else:
#                 vals_q.append(None)
#             if now_node.right:
#                 tmp_q.append(now_node.right)
#             else:
#                 vals_q.append(None)
#         print(vals_p, vals_q)
#         return vals_p == vals_q

class Solution:
    def isSameTree(self, p, q):
        # tmp_p = deque()
        # tmp_q = deque()
        # tmp_p.append(p)
        # tmp_q.append(q)
        # while tmp_p and tmp_q:
        #     p_now_node = tmp_p.popleft()
        #     q_now_node = tmp_q.popleft()
        #     if p_now_node.val == q_now_node.val:
        #
        #         if p_now_node.left:
        #             tmp_p.append(p_now_node.left)
        #         if p_now_node.right:
        #             tmp_p.append(p_now_node.right)
        #
        #         if q_now_node.left:
        #             tmp_p.append(q_now_node.left)
        #         if q_now_node.right:
        #             tmp_p.append(q_now_node.right)
        #     else:
        #         return False
        # return True


        if not p and not q: # 여기선 and가 쓰임
            return True
        if not p or not q: # 여기선 or이 쓰임
            return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) # 재귀로 들어간다





if __name__=="__main__":
    k = Solution()

    c1 = TreeNode(3)
    b1 = TreeNode(2)
    a1 = TreeNode(1,b1, c1)

    c2 = TreeNode(3)
    b2 = TreeNode(2)
    a2 = TreeNode(1, c2, b2)

    print(k.isSameTree(a1, a2))
    print(k.isSameTree(a1, a1))

# 위 코드 전부 [1,2] / [1, null, 2]에서 Wrong 걸림
