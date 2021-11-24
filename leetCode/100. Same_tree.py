'''
2개의 트리가 같은지, 확인하기
'''

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p, q):
        first, second = [], []
        queue = deque()

        queue.append(p)
        while len(queue) != 0:
            node = queue.popleft()
            first.append(node.val)
            if node.left != None:
                queue.append(node.left)
                first.append(node.left.val)
            elif node.left == None:
                first.append(0)

            if node.right != None:
                queue.append(node.right)
                first.append(node.right.val)
            elif node.right == None:
                first.append(0)

        queue.append(q)
        while len(queue) != 0:
            node = queue.popleft()
            second.append(node.val)
            if node.left != None:
                queue.append(node.left)
                second.append(node.left.val)
            elif node.left == None:
                second.append(0)

            if node.right != None:
                queue.append(node.right)
                second.append(node.right.val)
            elif node.right == None:
                second.append(0)
        print(first, second)
        return True if first == second else False

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