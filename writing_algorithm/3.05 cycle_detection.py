'''
중복된 값이 없는 연결 리스트에 순환이 있는지 검출하기
'''

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def test(root):
    tmp = set()
    tmp.add(root.val)
    root = root.next
    while root != None:
        if root.val in tmp:
            return True
        else:
            tmp.add(root.val)
            root = root.next
    return False

if __name__=="__main__":
    six = Node(61, None)
    five = Node(81, six)
    four = Node(31, five)
    three = Node(41, four)
    two = Node(21, three)
    one = Node(11, two)
    six.next = three # 여기서 순환 있음.

    print(test(one))