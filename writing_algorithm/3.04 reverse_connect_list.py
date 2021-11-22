'''
연결 리스트를 역으로 뒤집어 보자.
'''

class Node:
    def __init__(self, val = 0, next=None):
        self.val = val
        self.next = next

def test(root):
    tmp = [] # 임시 리스트 생성.

    while root.next != None:
        tmp.append(root.val)
        root = root.next
    tmp.append(root.val) # 마지막에 한 번 해 줘야, 끝 노드도 들어간다.

    root = None
    result_root = None
    for i in range(0, len(tmp)):
        if i == 0:
            root = Node(tmp.pop())
            result_root = root
        else:
            root.next = Node(tmp.pop())
            root = root.next

    return result_root

if __name__=="__main__":
    fourth = Node(45, None)
    third = Node(33, fourth)
    second = Node(22, third)
    first = Node(11, second)

    result = test(first)

    while result != None:
        print(result.val, end=' ')
        result = result.next