
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def mergeTrees(root1, root2): # 반환도 트리 형태로 나와야 한다.
    values = []
    que = [root1]
    while que:
        node = que.pop(0)
        if node == None:
            values.append(None)
        else:
            values.append(node.val)
            if node.left:        que.append(node.left)
            else:                que.append(None)

            if node.right:       que.append(node.right)
            else:                que.append(None)

    values2 = []
    que2 = [root2]
    while que2:
        node = que2.pop(0)
        if node == None:
            values2.append(None)
        else:
            values2.append(node.val)
            if node.left:        que2.append(node.left)
            else:                que2.append(None)

            if node.right:       que2.append(node.right)
            else:                que2.append(None)
    tmp = []
    for i in range(0, min(len(values), len(values2))):
        if values[i] == None and values2[i] != None:
            tmp.append(values2[i])
        elif values[i] != None and values2[i] == None:
            tmp.append(values[i])
        elif values[i] != None and values2[i] != None:
            tmp.append(values[i]+values2[i])
    print(tmp) # 이렇게 합치긴 했으나, 이 코드 가지고는 7 왼쪽에 있는 None은 표현 못함;;

d = TreeNode(5)
c = TreeNode(2)
b = TreeNode(3, d)
a = TreeNode(1, b, c)

ee = TreeNode(7)
dd = TreeNode(4)
cc = TreeNode(3, None, ee)
bb = TreeNode(1,None,dd)
aa = TreeNode(2, bb, cc)

print(mergeTrees(a, aa))
