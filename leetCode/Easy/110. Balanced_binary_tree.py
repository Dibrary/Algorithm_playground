
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(root):
    if root.left == None and root.right == None:
        return 1
    tmp = isBalanced(root.left)- isBalanced(root.right)

    if tmp >1:
        return False
    else:
        return True

# example은 통과했으나, submit에서 탈락.


'''
높이 균형을 맞추는 트리는 AVL 트리라고 한다. 

'''




### 책 풀이 ###

class Solution:
    def isBalanced(self, root):
        def check(root):
            if not root:
                return 0

            left = check(root.left)
            right = check(root.right)

            if left == -1 or right == -1 or abs(left-right) > 1:
                return -1
            return max(left, right) + 1
        return check(root) != -1


# 양쪽 자식 중 어느 하나라도 -1이 되면 계속 -1을 반환한다.

