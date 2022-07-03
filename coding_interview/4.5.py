
class Node:
    def __init__(self, val, left=None, right=None):
        self.val =val
        self.left = left
        self.right = right




f = Node(6)
e = Node(5)
d = Node(4)
c = Node(3)
b = Node(2)
a = Node(1)

c.left = b
c.right = d
b.left = a
d.right = e
e.right = f

def bfs(node):
    q = []
    q.append(node)

    flag = 0

    while q:
        node = q.pop(0)
        if node.left:
            if node.left.val < node.val:
                pass
            else:
                flag = 1
                break
            q.append(node.left)
        if node.right:
            if node.right.val > node.val:
                pass
            else:
                flag = 1
                break
            q.append(node.right)
    if flag == 1:
        return False
    else:
        return True

print(bfs(c))



f = Node(6)
e = Node(5)
d = Node(4)
c = Node(3)
b = Node(2)
a = Node(1)

c.left = b
c.right = d
b.left = a
d.right = e
e.left = f


print(bfs(c))

