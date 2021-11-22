'''
중복된 값이 있는 연결 리스트에 순환이 있는지 검출하기
'''

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def test(root):
    tmp = []
    tmp.append((root.val, root.next.val)) # 현재 값과, 다음 값을 동시에 저장 해 둠.
    root = root.next
    while root != None:
        if (root.val, root.next.val) in tmp:
            return True
        else:
            tmp.append((root.val, root.next.val))
            root = root.next
    return False

if __name__=="__main__":
    seven = Node(71, None)
    six = Node(61, seven)
    five = Node(81, six)
    four = Node(61, five)
    three = Node(41, four)
    two = Node(21, three)
    one = Node(11, two)
    seven.next = three # 여기서 순환 있음.

    print(test(one))