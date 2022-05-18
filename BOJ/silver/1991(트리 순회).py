
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

n = int(input())

childrens = dict()
nodes = dict()

for _ in range(n):
    value, left, right = input().split()
    childrens[value] = [left, right]
    nodes[value] = Node(value)

for i in nodes.keys():
    left, right = childrens[i]
    if left != ".":
        nodes[i].left = nodes[left]
    if right != ".":
        nodes[i].right = nodes[right]

preorder_value = ""
def preorder(node):
    global preorder_value

    if node != None:
        preorder_value += node.value
        if node.left:
            preorder(node.left)
        if node.right:
            preorder(node.right)
preorder(nodes['A'])

order_value = ""
def order(node):
    global order_value
    if node != None:
        if node.left:
            order(node.left)
        order_value += node.value
        if node.right:
            order(node.right)
order(nodes['A'])

postorder_value = ""
def postorder(node):
    global postorder_value
    if node != None:
        if node.left:
            postorder(node.left)
        if node.right:
            postorder(node.right)
        postorder_value += node.value
postorder(nodes['A'])

print(preorder_value)
print(order_value)
print(postorder_value)