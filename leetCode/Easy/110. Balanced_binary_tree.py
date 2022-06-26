
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




