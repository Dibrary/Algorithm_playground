
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lowestCommon(root, p, q):
    values = []
    que = [root]
    while que:
        node = que.pop(0)
        values.append(node.val)
        if node.left:
            que.append(node.left)
        if node.right:
            que.append(node.right)
    p_index = values.index(p)
    q_index = values.index(q)
    ancestor, ancestor2 = 0, 0
    if p_index%2 == 0:
        ancestor = values[p_index-2]
    if q_index%2 == 0:
        ancestor2 = values[q_index - 2]

    return ancestor2 if values.index(ancestor) > values.index(ancestor2) else ancestor

h = TreeNode(3)
g = TreeNode(9)
f = TreeNode(7)
e = TreeNode(4)
d = TreeNode(0)
c = TreeNode(8)
b = TreeNode(2)
a = TreeNode(6)
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g
e.left = h

print(lowestCommon(a, 2, 8))


# test에서 부터 에러 남.

