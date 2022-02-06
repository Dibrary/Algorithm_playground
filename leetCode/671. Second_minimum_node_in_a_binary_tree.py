
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findSecondMinimumValue(root):

    values = []
    q = []
    q.append(root)
    while q:
        node = q.pop(0)
        values.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

    values.sort()
    if values[-1] == values[-2] and values[-2] != min(values):
        return -1
    else:
        return values[-2]


# 틀림, 예외가 꽤 많다.


